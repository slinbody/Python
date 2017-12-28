#!/usr/bin/python3
import sqlite3

class sqlite_class:
    def __init__(self):
        db_file = '/home/user/net.db'
        self.conn = sqlite3.connect(db_file)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, type, value, traceback):
    '''
    it is necessry to privode type, value, traceback exception handing
    '''
        self.conn.close()

a = sqlite_class()
with a as cursor:
    for i in c.execute('select NAME,STATUS from XYFTTB'):
        print(i)
