#!/usr/bin/python
import sys
from memory_status import memory, resident, stacksize
import os
_proc_status = '/proc/%d/status' % os.getpid()

#class car(object): # new
class car():   # classic
    def __init__(self):
        self.wheel = 4

    def car_wheel(self):
        print 'I have {} wheel'.format(self.wheel)

class small_Car(car):
   def test():
       print "test"

#    def car_wheel(self):
#        super(samll_Car, Car).car_wheel.__get__(self)

if __name__ == '__main__':
    x1 = memory(_proc_status)
    x2 = resident(_proc_status)
    x3 = stacksize(_proc_status)
    print x1,x2,x3

    c = small_Car()
    c.car_wheel()
    print c.wheel
    i = range(1000000)
    tmp = 0
    for x in i:
        tmp = tmp + x

    x1 = memory(_proc_status, x1)
    x2 = resident(_proc_status, x2)
    x3 = stacksize(_proc_status, x3)
    print "memory, resident , stacksize"
    print x1,x2,x3
