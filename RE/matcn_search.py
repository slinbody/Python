#!/usr/bin/python
import re
ip = '11111000101010000000000100000000'
m1 =re.match('1+',ip)  # search from begining of string, must match at begining
print m1.group()
m2 = re.search('1+',ip)  # search throught string to find the first match position and stop
print m2.group()
m3 = re.findall('1+', ip)  # search throght string and print all match string
print m3

for i in re.finditer('1+', ip):
    print i.group()

s1='2017-11-29 Wed 10:08:48 192.168.16.16: PING GOOD, TRACEROUTE GOOD'
pattern='[\w]+ (?=GOOD)'
re.findall(pattern, s1)   # result:  ['PING ', 'TRACEROUTE ']
