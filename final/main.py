# -*- coding: utf-8 -*-
import binascii
import traceback

import nfc
import time
import requests
from threading import Thread, Timer
import json
import subprocess
import random

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

idms = {'0123456789012345':"ほげーた"}

# for i,j in json_dict.items():
#    print(i,j)

def notify_in_out(txt):
    WEB_HOOK_URL = 'https://hooks.slack.com/services/******'
    requests.post(WEB_HOOK_URL, data=json.dumps({
        "text" :txt,
    }))

if __name__ == '__main__' :

    absolutePath='/opt/in_out/'
    with open(absolutePath+'in_out.json','r') as f:
        json_dict = json.load(f)

    for idm in idms.values():
        if not idm in json_dict.keys():
            json_dict[idm] = 0

    try: 
        clf = nfc.ContactlessFrontend('usb:072f:2200')
    except OSError as e:
        subprocess.Popen(["lsusb"]).communicate()
        traceback.print_exc()
        raise

    while True:
        target_res = clf.sense(target_req_suica, iterations=int(TIME_cycle//TIME_interval)+1 , interval=TIME_interval)
        if target_res is not None:
            tag = nfc.tag.activate_tt3(clf, target_res)
            tag.sys = 3
            idm = binascii.hexlify(tag.idm)
            idm_str=idm.decode('utf-8')
            if idm_str in idms.keys():
                if(json_dict[idms[idm_str]] == 0): #入室した時
                    # subprocess.Popen(['mpg123',absolutePath+'in/okaeri.mp3'])
                    subprocess.Popen(['aplay',absolutePath+'in/okaeri.wav'])
                    json_dict[idms[idm_str]]=1
                    notify_in_out(idms[idm_str]+'が入室しました')
                else: #退室した時
                    # subprocess.Popen(['mpg123',absolutePath+'out/sayonara.mp3'])
                    subprocess.Popen(['aplay',absolutePath+'out/sayonara.wav'])
                    json_dict[idms[idm_str]]=0
                    notify_in_out(idms[idm_str]+'が退室しました')
            print(idm_str)
            with open(absolutePath+'in_out.json','w') as fw:
                json.dump(json_dict,fw,indent=2,ensure_ascii=False)
            time.sleep(TIME_wait)
        #end if
    #end while
    clf.close()
