#!/usr/bin/python3
from scapy.all import *
import datetime 
import time

def fun1(p):
    print('{} {} '.format(p[IP].src, p[IP].dst))
    print(p[Raw].load)

if __name__ == '__main__':
#    nic='ens192'
    nic='ens224'
    sniff(iface=nic, prn=fun1)
