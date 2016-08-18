#!/usr/local/bin/python
'''
檢查檔案是否有被修改，有則讀出並顯示
'''
import os
import subprocess
from time import sleep

filename = '/tmp/free.wife'
oldinfo = ''

while True:
    try:
        statinfo = str(os.stat(filename)).split(',')[8]
    except OSError:
        continue


    if statinfo != oldinfo:
        with open(filename,'r') as f:
            subprocess.call('clear',shell=True)
            print(f.read())

    oldinfo = statinfo
    sleep(0.2)


