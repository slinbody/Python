#!/usr/bin/python3 -u
'''
將圖片從redis讀出來
透過CGI輸出到網頁上
'''
import redis,sys
queue = redis.StrictRedis(host='localhost')

print("Content-Type:image/jpg")     # 需指定header
print()                             # 此行須存在

bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(queue.get('505'))
bstdout.flush()
