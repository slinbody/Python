#!/usr/bin/python
# 1 ~ 100會出現顏色變化
from __future__ import print_function
for i in range(1,1000):
    sys.stdout.write('\033[38;5;'+str(i)+'m'+str(i)+'\033[0m  ')
    if (i % 10) == 0:
         print ''
