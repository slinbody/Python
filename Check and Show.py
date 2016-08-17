#!/usr/local/bin/python
'''
檢查檔案是否有被修改，有則讀出並顯示
'''
import os
import subprocess
from time import sleep

filename = '/etc/config/api_request_result.conf'
oldinfo = ''

while True:
#    if not os.path.exists(filename):              touch出來的
#        os.system('touch '+filename)              會清掉之前結果，要改

    statinfo = str(os.stat(filename)).split(',')[8]

    if statinfo != oldinfo:
        with open(filename,'r') as f:
            subprocess.call('clear',shell=True)
            print(f.read())

    oldinfo = statinfo
    sleep(0.2)


