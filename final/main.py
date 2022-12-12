# -*- coding: utf-8 -*-
import binascii
import os
import traceback

import nfc
import time
import requests
import json
import subprocess

from member import Member

# Suica待ち受けの1サイクル秒
TIME_cycle = 1.0
# Suica待ち受けの反応インターバル秒
TIME_interval = 0.2
# タッチされてから次の待ち受けを開始するまで無効化する秒
TIME_wait = 2

# NFC接続リクエストのための準備
# 212F(FeliCa)で設定
target_req_suica = nfc.clf.RemoteTarget("212F")
# 0003(Suica)
target_req_suica.sensf_req = bytearray.fromhex("0000030000")

print('Suica waiting...')

def notify_in_out(txt):
    WEB_HOOK_URL = 'https://hooks.slack.com/services/******'
    requests.post(WEB_HOOK_URL, data=json.dumps({
        "text": txt,
    }))


if __name__ == '__main__':
    workdir = os.getcwd()

    try:
        clf = nfc.ContactlessFrontend('usb:072f:2200')
    except OSError as e:
        subprocess.Popen(["lsusb"]).communicate()
        traceback.print_exc()
        raise

    while True:
        target_res = clf.sense(target_req_suica, iterations=int(TIME_cycle//TIME_interval)+1, interval=TIME_interval)
        if target_res is not None:
            tag = nfc.tag.activate_tt3(clf, target_res)
            tag.sys = 3
            idm = binascii.hexlify(tag.idm)
            idm_str = idm.decode('utf-8')

            Member.load_members(workdir)

            if idm_str in Member.members:
                if Member.members[idm_str].state == 0:  # 入室した時
                    subprocess.Popen(['aplay', workdir + 'in/okaeri.wav'])
                    Member.members[idm_str].state = 1
                    notify_in_out(Member.members[idm_str].name + 'が入室しました')
                else:  # 退室した時
                    subprocess.Popen(['aplay', workdir + 'out/sayonara.wav'])
                    Member.members[idm_str].state = 0
                    notify_in_out(Member.members[idm_str].name + 'が退室しました')

            print(idm_str)
            Member.store_members(workdir)

            time.sleep(TIME_wait)
        # end if
    # end while
    clf.close()
