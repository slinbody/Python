#!/usr/local/bin/python3

f = open ('ttt','rb+')
f.write(b'9123456789abcdef')
f.seek(0)
print(f.read(1))
print(f.read(1))
print(f.read(1))
f.seek(5)
print(f.read(1))
print(f.read(1))
f.close()
