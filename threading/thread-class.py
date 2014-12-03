#!/usr/bin/python3
import threading

class Mythread(threading.Thread):
    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)
# subclass Thread object
# per-thread state information
# shared objects, not globals
    def run(self):
# run provides thread logic
        for i in range(self.count):
# still sync stdout access
            with self.mutex:
                print('[%s] => %s' % (self.myId, i))

stdoutmutex = threading.Lock()
threads = []

for i in range(10):
    thread = Mythread(i, 100, stdoutmutex)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print('Main thread exiting.')
