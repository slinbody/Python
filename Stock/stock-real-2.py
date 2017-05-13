#!/usr/bin/python
# -*- coding: utf8 -*-
'''
抓證交所的股票收盤資料
ref https://github.com/Asoul/tsrtc for detail
suck http://mis.twse.com.tw/stock/api/getStockInfo.jsp?json=1&delay=0&ex_ch=%20tse_1101.tw|tse_0050.tw
'''
import time
import json
import requests
import sys

def show_realtime(kind, *stock_id):
    twse_url = 'http://mis.twse.com.tw/stock/api/getStockInfo.jsp'
    timestamp = int(time.time() * 1000 + 1000)
    kind = "{}_".format(kind)
    channels = '|'.join(kind+'{}.tw'.format(target_tse) for target_tse in stock_id)
    query_url = '{}?&ex_ch={}&json=1&delay=0&_={}'.format(twse_url, channels, timestamp)
#    headers = {'Accept-Language': 'zh-TW','User-Agent': 'My User Agent 1.0',}
    headers = {'Accept-Language': 'zh-TW','User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',}
    req = requests.session()
    req.get('http://mis.twse.com.tw/stock/index.jsp', headers=headers)
    response = req.get(query_url)
#    print response.text
    if response.text.strip() == '':
        return 'nothing'

    content = json.loads(response.text, 'utf-8')
    data = content['msgArray']
#    return '\n'.join(x['n']+" : "+x['z']+","+x['t'] for x in data)
#    return data
    return '\n'.join([u'{n:10} {z:10} {t:10}'.format(**_) for _ in data])



if __name__ == '__main__':
    print show_realtime('tse', '1111','2222','3333')
    print show_realtime('otc', '4444')
    print time.strftime("%H:%M:%S")
