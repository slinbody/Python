#!/usr/bin/python3
from scapy.all import *
from group_info import market_data
import datetime 
import time
import random
import signal
import sys
from info import nic_info, src_info


def ip_to_binary(ip):
    octet_list_int = ip.split(".")
    octet_list_bin = [format(int(i), '08b') for i in octet_list_int]
    binary = ("").join(octet_list_bin)
    return binary

def get_addr_network(address, mask):
    #Convert ip address to 32 bit binary
    ip_bin = ip_to_binary(address)
    net_mask = ip_to_binary(mask)
    net_size = 0
    for i in net_mask:
        net_size = net_size + int(i)
    #Extract Network ID from 32 binary
    network = ip_bin[0:net_size]    
    return network

def check_in_subnet(ip1, ip2, mask):
    return get_addr_network(ip1, mask) == get_addr_network(ip2, mask)

def Exit_gracefully(signal, frame):
    print('Bye Bye !!')
    sys.exit(0)

def main(src_ip):
    seq_num = 0
    while True:
        for src in src_ip:
            for dst in market_data:
                data = str(datetime.datetime.now().strftime('%H:%M:%S'))
                data = 'taifex-' + data
                data = data + '-' + market_data[dst]['market-group']
                data = data + '-' + str(seq_num)
                p = IP(src=src[0], dst=dst)/UDP(sport=6666, dport=market_data[dst]['port'])/Raw(data)
#                send(p, iface='ens192', verbose=0)
                p = Ether(src=src[2])/p
                sendp(p, iface=src[1], verbose=0)
        seq_num = seq_num + 1
        time.sleep(1)

def src_analysis():
    src_ip = []
    for i in src_info:
        for j in nic_info:
            if check_in_subnet(i, nic_info[j]['IP'], nic_info[j]['MASK']):
                src_ip.append([i, j, nic_info[j]['MAC']])

    return src_ip

if __name__ == '__main__':
    print('Starting the following md testing:')
    print('-'*50)
    for key in sorted(market_data):
        print('{:16} {:16} {}'.format(market_data[key]['market-group'], key, market_data[key]['port']))
    signal.signal(signal.SIGINT, Exit_gracefully)

    src_ip = src_analysis()
    main(src_ip)
#    for i in src_ip:
#        print(i)
