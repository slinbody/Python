#!/usr/bin/python3 -u
'''
利用python3 -m http.server
來讀取圖檔
'''
import os
import sys

FILE_NAME = "/home/pi/cgi-bin/main.png"

baseName = os.path.basename(FILE_NAME)

#writing headers
#print("Content-Type:image/png; name=\"{0}\"".format(baseName))
#print("Content-Disposition: attachment; filename=\"{0}\"".format(baseName));
print()


bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(open(FILE_NAME,'rb').read())
bstdout.flush()
