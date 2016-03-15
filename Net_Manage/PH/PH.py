#!/usr/bin/python3
##  檢查目前是否為上課時間，若是則打開網路，不然關閉網路
import datetime
import pymysql
import sys
import telnetlib

def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    return start <=  x <= end

def convert_time(y):
    """轉換成時間"""
    y=y.split(':')
    return datetime.time(int(y[0]),int(y[1]))

def Network_Status():
    db = pymysql.connect(host="localhost", user="root", passwd="nturwa", db="IPDB", charset='utf8')
    cursor = db.cursor()
    cursor.execute("select Port_Status from PH_ROOM where ROOM_NAME='208';")
    result = cursor.fetchall()
    return result[0][0]

def Update_DB_Status(value):
    now = datetime.datetime.now()
    db = pymysql.connect(host="localhost", user="root", passwd="test", db="Your_DB_Name", charset='utf8')
    cursor = db.cursor()
    cursor.execute("update PH_ROOM set Port_Status = %s,time = %s where ROOM_NAME='208';",(value,now))
    result = cursor.fetchall()
    db.commit()

def Update_Port(value):
    tn = telnetlib.Telnet("1.1.1.5")
    tn.write(b'your_passwd'+b"\n") ## password
    tn.write(b"terminal length 0"+b"\n")
    tn.write(b"enable"+b"\n")
    tn.write(b"Your_enable_Passwd"+b"\n") ## enable password
    tn.write(b"config t"+b"\n")
    tn.write(b"int fa 0/13"+b"\n")
    if value : # 為 1 時，打開Port
        tn.write(b"no shutdown"+b"\n")
    else:      # 為 0 時，關閉Port
        tn.write(b"shutdown"+b"\n")
    tn.write(b"exit"+b"\n")
    tn.write(b"exit"+b"\n")
    tn.write(b"exit"+b"\n")
    output=tn.read_all().decode('utf-8')
    print(output)


####   主程式開始   #####
d=datetime.datetime.now()
with open('./'+d.strftime('%a'),'r') as f:  ##  讀出今天課表檔案
    lines = f.read().splitlines()
list_x=[]
for y in lines:                                 ##  讀出課表時間
    y = y.split()
    start = convert_time(y[0])
    start = (datetime.datetime.combine(datetime.datetime.today(),start) - datetime.timedelta(minutes=10)).time()
    ##  start是上課時間前十分鐘, type是datetime.time
    end = convert_time(y[1])
    end = (datetime.datetime.combine(datetime.datetime.today(),end) + datetime.timedelta(minutes=10)).time()
    ## end 是 下課時間的後十分鐘, type是datetime.time
    if time_in_range(start,end,datetime.datetime.now().time()):
    ## 如果現在時間在課程時間內，則為True
        classtime = True
        break

if classtime:
    if Network_Status() == 0: ## 在上課時間內，且Port未開
        Update_DB_Status(1)
        Update_Port(1)
        print('Port未開，請開')
else:
    if Network_Status():      ## 非上課時間內，且Port已開
        Update_DB_Status(0)
        Update_Port(0)
        print('Port已開，請關')
