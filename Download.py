#!/usr/bin/python3

import os
from urllib.parse   import quote
from urllib.request import urlopen
filename = '5.jpg'

remoteaddr = 'http://upload.wikimedia.org/wikipedia/zh/f/fe/'+quote('三重-金城五')+'5.jpg'

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
