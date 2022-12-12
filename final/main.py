# -*- coding: utf-8 -*-
import binascii
import os
import signal
import traceback

import nfc
import time
import subprocess

from member import Member


def sig_handler():
    global clf
    clf.close()


if __name__ == '__main__':
    WORKDIR = os.getcwd()

    # Suica待ち受けの1サイクル秒
    cycle_time = 1.0
    # Suica待ち受けの反応インターバル秒
    interval_time = 0.2
    # タッチされてから次の待ち受けを開始するまで無効化する秒
    sleep_time = 2

    # NFC接続リクエストのための準備
    # 212F(FeliCa)で設定
    target_req_suica = nfc.clf.RemoteTarget("212F")
    # 0003(Suica)
    target_req_suica.sensf_req = bytearray.fromhex("0000030000")

    print('Suica waiting...')

    try:
        clf = nfc.ContactlessFrontend('usb:072f:2200')
    except OSError as e:
        subprocess.Popen(["lsusb"]).communicate()
        traceback.print_exc()
        raise

    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    while True:
        target_res = clf.sense(target_req_suica, iterations=int(cycle_time // interval_time) + 1, interval=interval_time)
        if target_res is not None:
            tag = nfc.tag.activate_tt3(clf, target_res)
            tag.sys = 3
            idm = binascii.hexlify(tag.idm)
            idm_str = idm.decode('utf-8')

            Member.load_members(WORKDIR)

            if idm_str in Member.members:
                Member.members[idm_str].pass_gate()

            print(idm_str)
            Member.store_members(WORKDIR)

            time.sleep(sleep_time)
