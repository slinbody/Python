#!/usr/bin/python
# -*- coding: utf8 -*-
'''
抓證交所的股票收盤資料
this does not work since 2017/05/04
'''
import urllib2
from lxml import etree
import datetime
import telegram_bot

def get_today():
    year = str(int('20'+datetime.datetime.now().strftime("%y")) - 1911)
    today = datetime.datetime.now().strftime("/%m/%d")
    return year+today

def show_message(stock_id):
    title=['日期', '成交股數', '成交金額', '開盤價', '最高價', '最低價', '收盤價', '漲跌價差', '成交筆數']

    today = get_today()
    this_year = datetime.datetime.now().strftime("%Y")
    this_month = datetime.datetime.now().strftime("%m")
    url = "http://www.tse.com.tw/ch/trading/exchange/STOCK_DAY/STOCK_DAYMAIN.php"
    data = "download:&query_year="+this_year+"&query_month="+this_month+"&CO_ID="+stock_id+"&query_button='查詢'"

    request = urllib2.Request(url, data)
    f = urllib2.urlopen(url, data)

    html =  etree.HTML(f.read())
    tr_nodes = html.xpath("//table[@align='center']/tbody/tr")
    for tr_element in tr_nodes:
        if today == tr_element[0].text:
            ret_str = stock_id+" 今日消息:\n"
            for index, td_element in enumerate(tr_element):
                ret_str += "{}{} {}\n".format(title[index], ":", td_element.text)
            return ret_str

if __name__ == '__main__':
    print show_message('2892')


