#!/usr/bin/python3

import _thread as thread, time
def counter(myId, count):
  for i in range(count):
    time.sleep(1)
    print('[%s] => %s' % (myId, i)) # function run in threads

for i in range(5):
  thread.start_new_thread(counter, (i, 5)) # spawn 5 threads
# each thread loops 5 times
time.sleep(6)
print('Main thread exiting.')
