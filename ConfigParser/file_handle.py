#!/bin/python
# 先確認有 [ ] 存在
# 再用ConfigParser讀檔
fp = open(config_file, 'r')
pre = pos = 0
content = fp.readline()

whiel content:
    prev, pos = pos, fd.tell()
    if '[' in content and ']'  in content:
        fd.seek(prev)
        break
    content = fd.readline()

config = ConfigParser.SafeConfigParser()
config.readfp(fp)
fp.close()
