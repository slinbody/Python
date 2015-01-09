#!/usr/bin/python3

import os
from urllib.request import urlopen
filename = '5.jpg'

remoteaddr = b'http://upload.wikimedia.org/wikipedia/zh/f/fe/5.jpg'

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
