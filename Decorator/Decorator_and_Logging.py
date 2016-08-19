#!/usr/bin/python
'''
利用Decorator與Logging
紀錄程式執行經過
'''
import logging
import time

def Big(func):
    def Mid(*args,**kwargs):
        logger = logging.getLogger('decorator')
        logger.setLevel(logging.INFO)
        f_handle = logging.FileHandler("/tmp/test")
        formatter = logging.Formatter('%(asctime)s %(name)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
        f_handle.setFormatter(formatter)
        logger.addHandler(f_handle)
        print 'start of :'+func.__name__
        logger.info('start of  :'+func.__name__)
        func(*args,**kwargs)       #your function work here
        logger.info(func.__name__+'('+ ' '.join(str(i) for i in args) +')')
        print "  end of :"+func.__name__
        logger.info('end of  :'+func.__name__)
    return Mid


@Big
def add(x,y):
    print"x+y=",x+y

add(4,6)
