#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup as bs
import datetime

Stationnum={1009:'萬華',1008:'台北',1007:'松山',1031:'汐科'}

fromstation=str(1008)
tostation=str(1031)

now = datetime.datetime.now()
today = now.strftime("%Y/%m/%d")
fromtime= now.strftime("%H%M")
totime= (datetime.datetime.today() + datetime.timedelta(hours=2)).strftime("%H%M")

#--------  自訂時間 ---------
#today= '2016/08/01'
#fromtime= '0730'
#totime= '0900'
#----------------------------

if fromtime > totime:
        totime='2359'
#print(fromtime)

if now >  datetime.datetime.combine(datetime.datetime.today(),datetime.time(14, 0)):
        (fromstation,tostation)= (tostation,fromstation)

rs = requests.get('http://twtraffic.tra.gov.tw/twrail/SearchResult.aspx?searchtype=0&searchdate='+today+'&fromcity=0&tocity=0&fromstation='+fromstation+'&tostation='+tostation+'&trainclass=2&timetype=1&fromtime='+fromtime+'&totime='+totime)

#soup = bs(rs.text,"html5lib")
#soup = bs(rs.text,"html.parser") # use this if on window platform
soup = bs(rs.content,"html5lib")
#print(soup.prettify())

#print("萬華1009  台北1008  松山1007  汐科1031")
print(today+' '*12+Stationnum[int(fromstation)]+" 往 "+Stationnum[int(tostation)])

table = soup.find('table',attrs={'id':'ResultGridView'})
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
        cols = row.find_all('td')
        x = [element.text.strip() for element in cols]
        print(x[0],x[1],x[3],x[4],x[5],x[6])


