#!/usr/bin/python
'''
10秒內沒收到'kill -USR1 PID',就結束程式
每收到'kill -USR1 PID', time就更新為10
使用Global變數的方法來寫
'''
import signal
import os
import time
i=10
def receive_signal(signum, stack):
    global i
    print 'Received:', signum
    i = 10

signal.signal(signal.SIGUSR1, receive_signal)
print 'My PID is:', os.getpid()

while i>0:
    print 'i: ',i
    i = i - 1
    time.sleep(3)
