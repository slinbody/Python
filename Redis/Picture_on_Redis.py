#!/usr/bin/python3 -u
'''
將Redis上的圖片，隨機讀出
透過CGI送到網頁上
'''
import redis,sys
import time
import random
queue = redis.StrictRedis(host='localhost')
Pic_List = ['1','505']

print("Content-Type:image/jpg")
print()

bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(queue.get(Pic_List[random.randrange(0,2)]))
bstdout.flush()
