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
pattern='[\w]+ (?=GOOD)'       # ?=表示從匹配此pattern的位置可以找
re.findall(pattern, s1)        # result: ['PING ', 'TRACEROUTE ']
pattern="(?<=PING )[\w]+"
re.findall(ping_pattern, s1)   # result: ['GOOD']

delay_pattern = 'delay data for tr_code=1,msg_kind=2,seq=([\d]+),'
str1 = 'delay data for tr_code=1,msg_kind=2,seq=1671,'
p1 = re.compile(delay_pattern)
p1.findall(str1)    # ['1671']

lost_pattern = 'lost data for tr_code=1,msg_kind=2,from ([\d]+) to ([\d]+),'
str2 = 'lost data for tr_code=1,msg_kind=2,from 11 to 66,'
p2 = re.compile(lost_pattern)
p2.findall(str2)    # [('11', '66')]
