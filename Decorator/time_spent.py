#!/usr/bin/python
import time

def time_run(func):
    def Mid(*args, **kwargs):
        print 'start of : '+func.__name__
        start  = time.time()
        func(*args, **kwargs)
        end = time.time()
        print 'end of :'+func.__name__
        print '{0} time spent: {1:3f}'.format(func.__name__,(end - start))
    return Mid

@time_run
def Isleep(z):
    time.sleep(5)

@time_run
def add(x,y):
    print"x+y=",x+y

if __name__ == '__main__':
    Isleep(1)
    print ''
    add(1,2)
'''
result:
start of : Isleep
end of :Isleep
Isleep time spent: 5.005279

start of : add
x+y= 3
end of :add
add time spent: 0.000074
'''
