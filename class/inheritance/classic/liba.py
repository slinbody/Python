#!/usr/bin/python
import sys

#class car(object): # new
class car():   # classic
    def __init__(self):
        self.wheel = 4

    def car_wheel(self):
        print 'I have {} wheel'.format(self.wheel)

class small_Car(car):
    def __init__(self):
        self.size='small'
#        super(small_Car, self).__init__()  # new
        car.__init__(self)   # classic

    def car_size(self):
        print 'My size is '+self.size

#    def car_wheel(self):
#        super(samll_Car, Car).car_wheel.__get__(self)

if __name__ == '__main__':
    c = small_Car()
    c.car_size()
    c.car_wheel()
    print c.wheel
