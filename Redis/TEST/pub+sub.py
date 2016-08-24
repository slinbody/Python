#!/usr/bin/python3
'''
將sub和pub寫在一起
'''
import time
import redis
queue = redis.StrictRedis(unix_socket_path='/tmp/redis.sock')
channel = queue.pubsub()
channel.subscribe('test')
Input = ''

while True:
#    Input = input('What u want to show: ')
    if Input:
        queue.publish("test", Input)

#        p = channel.subscribe('test')
    message = channel.get_message()
    if message:
        print("You Input : ", message['data'])
    Input = input('What u want to show: ')
    time.sleep(0.2)
