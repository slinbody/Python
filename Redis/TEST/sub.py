#!/usr/bin/python2.7
'''
讀取訊息
'''
import redis
import time

#r = redis.StrictRedis(host='localhost', port=6379, db=0)           #用網路連
r = redis.StrictRedis(unix_socket_path='/tmp/redis.sock')    #用socket連
p = r.pubsub()
p.subscribe('test')

while True:
    message = p.get_message()
    if message:
        print "Subscriber: %s" % message['data']
    time.sleep(1)
