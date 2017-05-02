#!/usr/bin/python
# -*- coding: utf8 -*-
'''
抓證交所的股票收盤計錄資料
'''
import urllib2
from lxml import etree

def show_message(stock_id):
    title=['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']

    url = "http://www.tse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php"
    data = "download:&query_year=2017&query_month=4&CO_ID="+stock_id+"&query_button='查詢'"
    request = urllib2.Request(url, data)
    f = urllib2.urlopen(url, data)
#    print f.read()

    html =  etree.HTML(f.read())
    tr_nodes = html.xpath("//table[@align='center']/tbody/tr")
    for tr_element in tr_nodes:
        for index, td_element in enumerate(tr_element):
            print "{}{} {}".format(title[index], ":", td_element.text)
        print "\n"

if __name__ == '__main__':
    show_message('2412')
