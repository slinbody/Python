#!/usr/bin/python3

import _thread as thread, time
  fd = open('/tmp/thread-test','a+')
  for i in range(count):
    time.sleep(1)
    fd.write('thread [%s] => 第%s次\n' % (myId,i))
  fd.close()


for i in range(5):
  thread.start_new_thread(counter, (i, 5)) # spawn 5 threads
# each thread loops 5 times
time.sleep(6)  # 若無此行，就結束，thread跟著結束
print('Main thread exiting.')
