#!/usr/bin/python
import ConfigParser

config = ConfigParser.ConfigParser()
filename = '/home/pi/myproject/test.ini'
fd = open(filename,'r+')
config.readfp(fd)

print config.get('My Section','foodir')
print config.get('My Section','dir1')

if not config.has_section('Section2'):
    config.add_section('Section2')
config.set('Section1', 'an_int', '09915')
config.set('Section2', 'a_bool', 'true')
config.set('Section2', 'a_float', '3.1415')
config.set('Section1', 'baz', 'funny')
config.set('Section1', 'bar', 'Python')
config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

fd.seek(0)
config.write(fd)
fd.close()
