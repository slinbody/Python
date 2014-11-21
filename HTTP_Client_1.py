#!/usr/bin/python3
import http.client
url1=input("Your Web Link:\n")
conn = http.client.HTTPConnection(url1)
conn.request("HEAD","/v3/main.php")
r1 = conn.getresponse()
print(r1.status,r1.reason)
