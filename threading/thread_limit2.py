# another way to implement without class

import Queue
import threading, time

def fff(queue1, name):
    global b_list
    while not queue1.empty():
        i = queue1.get()
        print "{}: {}".format(name, i)
        b_list.append(i)
        queue1.task_done()
        time.sleep(2)


queue1=Queue.Queue()
THINGS = ['item%02d'%i for i in range(100)]
AVAILABLE_CPUS=8


for thing in THINGS:
    queue1.put(thing)

b_list=[]
threads = []
for OneOf in range(AVAILABLE_CPUS):
    name = "Thread-{}".format(OneOf)
    thread=threading.Thread(target=fff, args=(queue1, name,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print b_list
