#!/usr/bin/python3

import datetime
year = 2017
month = 11

for i in range(1,31):
    x = datetime.datetime(year, month, i)
    if x.weekday()  < 5:
        print(x.strftime("%Y/%m/%d %A"))
        
## result
2017/11/01 Wednesday
2017/11/02 Thursday
2017/11/03 Friday
2017/11/06 Monday
2017/11/07 Tuesday
2017/11/08 Wednesday
2017/11/09 Thursday
2017/11/10 Friday
2017/11/13 Monday
2017/11/14 Tuesday
2017/11/15 Wednesday
2017/11/16 Thursday
2017/11/17 Friday
2017/11/20 Monday
2017/11/21 Tuesday
2017/11/22 Wednesday
2017/11/23 Thursday
2017/11/24 Friday
2017/11/27 Monday
2017/11/28 Tuesday
2017/11/29 Wednesday
2017/11/30 Thursday


