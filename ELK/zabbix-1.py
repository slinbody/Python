#!/usr/bin/python3
import requests
from pprint import pprint
import json
from datetime import datetime, timedelta
import re
from sendmail import sent


ZABIX_ROOT = 'http://localhost/zabbix'
url = ZABIX_ROOT + '/api_jsonrpc.php'

headers = {
    'content-type': 'application/json',
}

def get_auth_value():
    payload = {
        "jsonrpc" : "2.0",
        "method" : "user.login",
        "params": {
          'user': 'admin',
          'password':'admin',
        },
        "id" : 0,
    }

    headers = {
        'content-type': 'application/json',
    }

    res  = requests.post(url, data=json.dumps(payload), headers=headers)
    res = res.json()
#    print('user.login response')
#    pprint(res)
    return res['result']

def get_hostid(auth_value, hostname):
    payload = {
        "jsonrpc" : "2.0",
        "method" : "host.get",
        "params": {
          'output': ['hostid',
                     'name',
                    ],
###
          'filter':{
              "host":[hostname]
          },
###
        },
        "auth" : auth_value,
        "id" : 2,
    }

    headers = {
        'content-type': 'application/json',
    }

    res = requests.post(url, data=json.dumps(payload), headers=headers)
    res = res.json()
#    pprint(res)
    #print('host.get response')
    for content in res['result']:
        print(content['name'])
#        if hostname in content['name']:
#            break
    if len(res['result']) == 1:
        return res['result'][0]['hostid']
    else:
        return 'More than 2 hosts'

def get_item_id(host_name, auth_value, item_name):
    payload = {
        "jsonrpc":"2.0",
        "method":"item.get",
        "params":{
            "output":["itemids", "name" ],
#            "output":"extend",
            "host" : host_name,
#            "sortfield":"name",
            "search":{#"name":["ge-0/0/0", "ge-0/0/8", "ge-1/0/4", "ge-1/0/12"],
#                      "name":["ge-0/0/0","Bits"],
                      "name":[item_name, "Bits"],
#                      "name":"ge-1/0/4",
#                      "name":"ge-1/0/12",
#                      "name":"Bits sent",
            },
#            "searchByAny":True,
#            "searchWildcardsEnabled": True,
        },
       "auth" : auth_value,
       "id" : 4,
    }


    res = requests.post(url, data=json.dumps(payload), headers=headers)
    res = res.json()

    max_res = {}
    for content in res['result']:
#        if item_name in content['name'] and 'Bit' in content['name']:
#        print(content['name'])
        max_time, max_bw = get_history_data(auth_value, content['itemid'])
        m = re.search(r"\(([A-Za-z0-9_-]+)\):\ Bits\ ([A-Za-z]+)$", content['name'])
        device_name = m.group(1)
        IN_OUT      = m.group(2)
        if IN_OUT == 'received':
            IN_OUT = 'IN'
        if IN_OUT == 'sent':
            IN_OUT = 'OUT'
#        print(device_name, IN_OUT)
        if not device_name in max_res.keys():
            max_res[device_name] = {}
        max_res[device_name][IN_OUT] = {'max_time':max_time, 'max_bw':max_bw}
    return max_res
#        return content['name'], get_history_data(auth_value, content['itemid'])
#        print("---------")

def get_history_data(auth_value, item_id):
    today = datetime.today()
    if today.isoweekday() in [ i for i in range(2,6) ]:
        delta = 1
    else:
        delta = 3

#    last_hr = datetime.now() - timedelta(hours = 1)
    last_hr = datetime.now() - timedelta(days = delta)
    last_hr = last_hr.timestamp()

    payload = {
        "jsonrpc": "2.0",
        "method": "history.get",
        "params": {
            "output": ["clock", "value"],
#            "history": 0,
            "itemids": item_id,
            "time_from": int(last_hr),
            "time_till": int(datetime.now().timestamp()),
            "sortfield": "clock",
#            "sortfield": "value",
#            "sortorder": "DESC",
#            "limit": 1,
        },
        "auth": auth_value,
        "id": 111
    }

    res = requests.post(url, data=json.dumps(payload), headers=headers)
    res = res.json()

    max_time, max_band = 0,0
    for content in res['result']:
        print(datetime.fromtimestamp(int(content['clock'])), content['value'])
        tmp_band = int(content['value'])
        if max_band < tmp_band:
            max_band = tmp_band
            max_time = content['clock']

    output_time = datetime.fromtimestamp(int(max_time)).strftime("%Y-%m-%d<br>%H:%M:%S")
    output_band = int(max_band) / 1000000
#    print("{}: {:,.2f} Mbps".format(output_time, output_band))
    return output_time, max_band
#    pprint(res)

if __name__ == '__main__':
    ifcs_list = ['ge-0/0/0(', 'ge-0/0/8(', 'ge-1/0/4(', 'ge-1/0/12(']
#    ifs_list = ['ge-0/0/0(']
    auth_value = get_auth_value()
#    host_value = get_hostid(auth_value, 'BQ-INT-SW-Ext')

    summary = [['device', 'port', "desc", "bw",'time', "Max_in<br>Mbits/sec", 'ratio', 'time','Max_out<br>Mbits/sec', 'ratio']]
    for ifcs in ifcs_list:
        res = get_item_id("BQ-INT-SW-Ext", auth_value, ifcs)
        key_name = list(res.keys())[0]
        IN_bw  = '{:.2f}Mbps'.format(int(res[key_name]['IN']['max_bw']) / 1000000)
        OUT_bw = '{:.2f}Mbps'.format(int(res[key_name]['OUT']['max_bw']) / 1000000)
        IN_ratio  = '{:.2f}%'.format(int(res[key_name]['IN']['max_bw']) / 100000000 * 100)
        OUT_ratio = '{:.2f}%'.format(int(res[key_name]['OUT']['max_bw']) / 100000000 * 100)

        summary.append(["BQ-INT-SW-Ext", ifcs[:-1], key_name, '100M', IN_bw, res[key_name]['IN']['max_time'], IN_ratio, OUT_bw, res[key_name]['OUT']['max_time'], OUT_ratio])

    for i in summary:
        print(i)


    sent(summary)

