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
        statinfo = os.stat(filename).st_mtime
    except OSError:
        continue

    if os.stat(filename).st_size == 0:
        continue

    if statinfo != oldinfo:
        with open(filename,'r') as f:
            subprocess.call('clear',shell=True)
            print(f.read())

    oldinfo = statinfo
    sleep(0.2)


