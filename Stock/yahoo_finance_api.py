#!/usr/bin/python
'''
use yhaoo_finace api to get stock information
#sudo pip install yahoo_finance
'''
from yahoo_finance import Share
import datetime

def getStock(id):
    stock = Share(str(id)+'.TW')
    today = datetime.date.today()
    data = stock.get_historical('2017-04-20', str(today))
#    data = stock.get_historical('2017-04-20', '2017-04-20')
#    data = stock.get_historical(str(today), str(today))
    return data

for _ in getStock(2412):
    print _
