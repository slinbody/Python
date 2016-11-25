#!/usr/bin/python
import itertools

a = [1,2,3,4,5,6]

izip(a,a[1:])

for i in itertools.izip(a,a[1:]):
    print i
    
#  -----  result ------
(1, 2)
(2, 3)
(3, 4)
(4, 5)
(5, 6)
