#!/usr/bin/python
import logging
import time

def Big(func):
    def Mid(*args,**kwargs):
        print 'start of  :'+func.__name__
        func(*args,**kwargs)       #your function work here
        print "end of :"+func.__name__
    return Mid


@Big
def add(x,y):
    print"x+y=",x+y

add(4,6)
