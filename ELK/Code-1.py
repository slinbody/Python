#!/usr/bin/python3
import sys
import requests
import json
from pprint import pprint

target = {'Outside':['192.168.203.121', 
                    ],
           'Inside':['192.168.203.233', 
                    ],
             '5Area':['192.168.204.211', 
                    ]
         }


ago_time = "now-1m"

def print_log(data):
    for i in data['hits']['hits']:
#        print(i['_source']['@timestamp'],i['_source']['message'])
        print(i['_source']['message'])

def main(hosts):
    url = 'http://localhost:9200/_search?scroll=10s'
#    url = 'http://localhost:9200/_search'
    payload = {
              "sort": [{"@timestamp":"desc"},
#                       {"host":"desc"} 
                      ],
              "from":0, "size":10000,
              "query": {
                "bool":{
                  "must":[
                    {
                      "range":{
                          "@timestamp": {
                              "gte": ago_time,
#                              "lte": "now"
                          }
                      }
                    },
                    {
                      "match":{
                          "host":hosts
                      }
                    }
                  ], # end of must
#                  "should":[
#                    {
#                      "match":{
#                          "host":"192.168.203.121"
#                      }
#                    },
#                    {
#                      "match":{
#                          "host":"192.168.203.123"
#                      }
#                    }
#                  ]  # end of should
                }
              }
            }

    header = {"content-type": "application/json"}
    response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
    data = response.json()
    print_log(data)
#    print('hits len: {}, total: {}'.format(len(data['hits']['hits']),data['hits']['total']))

#    count = 0
    while len(data['hits']['hits']) > 0 :
        scroll_id = data['_scroll_id']
        url = 'http://localhost:9200/_search/scroll'
        payload = { "scroll": "10s",
                    "scroll_id": scroll_id
                  }
        header = {"content-type": "application/json"}
        response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
        data = response.json()
        print_log(data)
#        print('='*30)
#        print('count: {}'.format(count))
#        count = count + 1
#        pprint(data)
#        print('hits len: {}, total: {}'.format(len(data['hits']['hits']),data['hits']['total']))


if __name__ == '__main__':

    obj = sys.argv[1] if len(sys.argv) > 1 else None
    if target.get(obj, None):
        hosts = ' '.join(i for i in target[obj])
        main(hosts)
    else:
        print('''
                 Usage: elastic-ql.py <location>
                 only 3 location:
                 1. Outside
                 2. Inside
                 3. 5Area
        ''')
