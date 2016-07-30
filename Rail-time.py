#!/usr/bin/python3
""" 查詢當日火車時間 """
import requests
from bs4 import BeautifulSoup as bs
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y/%m/%d")

rs = requests.get('http://twtraffic.tra.gov.tw/twrail/SearchResult.aspx?searchtype=0&searchdate='+today+'&fromcity=0&tocity=0&fromstation=1008&tostation=1005&trainclass=2&timetype=1&fromtime=0700&totime=1200')

soup = bs(rs.text,"html5lib")

table = soup.find('table',attrs={'id':'ResultGridView'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
        cols = row.find_all('td')
        x = [ele.text.strip() for ele in cols]
        print(x[0],x[3],x[4],x[5],x[6])
