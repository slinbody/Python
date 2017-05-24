#!/usr/bin/python
# -*- coding: utf8 -*-
'''
抓證交所的股票收盤資料
'''
import urllib2
from lxml import etree
import datetime
import telegram_bot
import json

object = {
'2412':'種花'
}

def get_today():
    year = str(int('20'+datetime.datetime.now().strftime("%y")) - 1911)
    today = datetime.datetime.now().strftime("/%m/%d")
    return year+today

def show_message(stock_id):
    title=['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']

    today = get_today()
    this_year = datetime.datetime.now().strftime("%Y")
    this_month = datetime.datetime.now().strftime("%m")

    url = "http://www.twse.com.tw/exchangeReport/STOCK_DAY"
    data = "date={}&stockNo={}".format(datetime.datetime.now().strftime("%Y%m%d"), stock_id)

    request = urllib2.Request(url, data)
    f = urllib2.urlopen(url, data)

    result = json.loads(f.read())
    for i in result['data']:
        if i[0] == get_today():
            ret_str = object[stock_id]+" 今日消息:\n"
            for index,_ in enumerate(title):
                ret_str += "{}{} {}\n".format(_, ":", i[index])
            return ret_str


    return "NO TRADE"

if __name__ == '__main__':
    for _ in object.keys():
        print show_message(_)

