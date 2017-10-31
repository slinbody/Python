#!/usr/bin/python3

import datetime
year = 2017
month = 11

for i in range(1,31):
    x = datetime.datetime(year, month, i)
    print(x.strftime("%Y/%m/%d"))
