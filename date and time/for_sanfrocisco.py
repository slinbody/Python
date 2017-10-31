#!/usr/bin/python3
"""
Sanfrocisco schdule
"""

import datetime
year = 2017
month = 11
weekday_dic = {0:'週一', 1:'週二', 2:'週三', 3:'週四', 4:'週五'}

for i in range(1,31):
    x = datetime.datetime(year, month, i)
    if x.weekday()  < 5:
#        str_1 = "{}年{}月{}日  {}".format(x.strftime("%Y"), x.strftime("%m"), x.strftime(%d), weekday_dic[x.weekday()])
        str_1 = x.strftime("%Y年%m月%d日  {}".format(weekday_dic[x.weekday()]))
        print(str_1+"小夜")
        print(str_1+"大夜")
