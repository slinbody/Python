#!/usr/bin/python
def Big(func):
    def Mid(*args,**kwargs):
        print 'function name :'+func.__name__
        print 'x = ',args[0],'y = ',args[1]
        return func(*args,**kwargs)
    return Mid


@Big
def add(x,y):
    print"x+y=",x+y

add(4,6)

'''
result:
function name :add
x =  4 y =  6
x+y= 10
'''
