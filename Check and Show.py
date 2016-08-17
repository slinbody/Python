#!/usr/local/bin/python
'''
檢查檔案是否有被修改，有則讀出並顯示
'''
import os
import subprocess
from time import sleep
filename = '/tmp/free_wife'
if not os.path.exists(filename):
    os.system('touch '+filename)
statinfo = str(os.stat(filename)).split(',')[8]
oldinfo = ''
while True:
    if statinfo != oldinfo:
        subprocess.call('clear',shell=True)
        with open(filename,'r') as f:
#        subprocess.call('clear',shell=True)
            print(f.read())
#        oldinfo = statinfo
    sleep(2)

