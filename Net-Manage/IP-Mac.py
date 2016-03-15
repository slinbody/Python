#!/usr/bin/python3
#紀錄Cisco 
#Core上所有IP MAC 對應

import telnetlib
import datetime
import pymysql
import re

#now = datetime.datetime.now()

host = "11.12.10.24" # your router ip
password = "your password"
#filename_prefix = "your file prefix-"

tn = telnetlib.Telnet(host)
tn.read_until(b"Password:")
tn.write(password.encode('ascii')+b"\n")
tn.write(b"terminal length 0"+b"\n")
tn.write(b"sh arp"+b"\n")
tn.write(b"exit"+b"\n")
output=tn.read_all().decode('utf-8')

db = pymysql.connect(host="localhost", user="root", passwd="DBpasswd", db="IPDB", charset='utf8')
cursor = db.cursor()
for line in output.splitlines():
    x=line.split()
    if "Internet" in x and "Incomplete" not in x:
        cursor.execute("insert into IP_By_Cron(IP,MAC) value (%s,%s);",(x[1],x[3]))
        result = cursor.fetchall()
db.commit()

#filename = "/tmp/%s_%.2i-%.2i-%i_%.2i-%.2i-%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour,now.minute,now.second)

#fp=open(filename,"w")
#fp.write(output)
#fp.close()
