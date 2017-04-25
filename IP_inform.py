#!/usr/bin/python
from urllib2 import urlopen
import smtplib
import datetime
import os.path

CurrentIP_record = "/tmp/CurrentIP"

def send_IP(my_ip):
    fromaddr = 'slinbody@gmail.com'
    toaddrs  = ['slinbody@gmail.com','slinbody@taifex.com.tw']
    subject = 'IP change'
    x = datetime.datetime.now()
    now = x.strftime("%b %d %H:%M:%S")

#    server = smtplib.SMTP('smtp.gmail.com:587')
#    server.starttls()
#    server.login(username,password)
    server = smtplib.SMTP("ms2.hinet.net")
    msg = 'Subject: %s: %s\n\n%s\n%s' % (subject, my_ip, my_ip, now)

    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

my_current_ip = urlopen('http://ip.42.pl/raw').read()
#print my_current_ip

if os.path.isfile(CurrentIP_record):
    with open(CurrentIP_record, "r+") as fd:
        tmp_IP = fd.read()
    #print tmp_IP
else:
    tmp_IP=''

if not my_current_ip == tmp_IP:
    print "NO EQ"
    send_IP(my_current_ip)
    with open(CurrentIP_record, "w") as fd:
        fd.write(my_current_ip)
else:
    print "NO CHANGE" 
