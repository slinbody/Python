#!/usr/local/bin/python3
"""顯示檔案的內容 """
name = input('檔案名稱：')
file = open (name,'r')
content = file.read()
print(content)
file.close()

