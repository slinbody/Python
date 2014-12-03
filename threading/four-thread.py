#!/usr/bin/python3
''' Compare threading and _thread module '''
import threading, _thread
def action(i):
    print(i ** 32)
# subclass with state

class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)
    def run(self):
        print(self.i ** 32)

Mythread(2).start()

thread = threading.Thread(target=(lambda: action(2)))
thread.start()

threading.Thread(target=action, args=(2,)).start() 

_thread.start_new_thread(action, (2,))
