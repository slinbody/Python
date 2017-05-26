#!/usr/bin/python
# -*- coding: utf8 -*-
# This is used to count the number of items

result = {}

with open('/tmp/menu') as fd:
    for line in fd:
        if line == '\n':
            continue

        line = line.replace('\n','')
        line = line.split('+')
        for x in line:
            x = x.replace(" ","").decode('UTF-8')
            if x not in result.keys():
#                print x
                result[x] = 1
            else:
                result[x] = result[x] + 1
    for (k,v) in result.items():
        print k,v
