#!/usr/bin/python
class A:
        def __init__(self):
                print "__init__"
 
        def __enter__(self):
                print "__enter__"
 
        def __exit__(self, exc_ty, exc_val, tb):
                print "__exit__"
 
a = A()
with a as x:
        print " in with x=%r" % x
