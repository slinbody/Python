# In the program, show you how to limit the number of threadings by Queue module
import Queue
import threading, time

class MyThread(threading.Thread):
    def __init__(self, theQueue=None):
        threading.Thread.__init__(self)
        self.theQueue=theQueue

    def run(self):
        while not self.theQueue.empty():
            thing=self.theQueue.get()
            self.process(thing)
            self.theQueue.task_done()

    def process(self, thing):
        time.sleep(1)
        print 'processing %s'%thing

queue=Queue.Queue()
THINGS = ['Thing%02d'%i for i in range(101)]
AVAILABLE_CPUS=3

for thing in THINGS:
    queue.put(thing)

for OneOf in range(AVAILABLE_CPUS):
    thread=MyThread(theQueue=queue)
    thread.start()

