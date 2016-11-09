#!/bin/python

def test(*one,**two):
  print one
  print "and"
  print two
  
  
test(1,2,3,a='1',b='2')

#---------result-----------
(1, 2, 3)
and
{'a': '1', 'b': '2'}
