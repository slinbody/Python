#!/usr/bin/python3
import sys
import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="DB-Password", db="IPDB", charset='utf8')
cursor = db.cursor()

st='select IP,MAC,Time from IP_By_Cron \
WHERE DATE(Time) = CURDATE() \
order by Time desc \
limit 10;'                                   #列出今天的紀錄

st='select IP,MAC,Time from IP_By_Cron where IP="192.168.119.32";'  #列出與IP 192.168.119.32 相關資料
#st='select IP,MAC,Time from IP_By_Cron where IP="'+sys.argv[1]+'";'  #列出與IP argv[1] 相關資料
#st='select IP,MAC,Time from IP_By_Cron where MAC="30b5.c257.7627";'  #列出與MAC xxxx.xxxx.xxxx 相關資料
cursor.execute(st)
result = cursor.fetchall()

for record in result:
    print(record[0].ljust(15)+"  "+record[1]+"  "+str(record[2]))
