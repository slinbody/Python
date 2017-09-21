

import csv
def getdata(filename):
    while True:
       with open(filename) as fd:
            for row in csv.reader(fd):
                yield row[0]
                
x = getdata('/tmp/dns_black.csv')

x.next()
x.next()
x.next()

for i in x:
    print i
