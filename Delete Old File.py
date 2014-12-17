import os
import datetime
for dirpath,dirnames,filenames in os.walk(dir_to_search):
    for file in filenames:
        curpath=os.path.join(dirpath,file)
        print(curpath)
