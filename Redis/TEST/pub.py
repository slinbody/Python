#!/usr/bin/python2.7
'''
送訊息
'''
import redis
import time

#queue = redis.StrictRedis(host='localhost', port=6379, db=0)            # 用網路連
queue = redis.StrictRedis(unix_socket_path='/tmp/netmgr-redis.sock')     # 用socket連
channel = queue.pubsub()

for i in range(10):
    queue.publish("test", i)
    time.sleep(0.5)
