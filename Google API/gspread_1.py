#!/usr/bin/python
# -*- coding: utf8 -*-
# Google Drive API test

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('mysheet.json', scope)
client = gspread.authorize(creds)

sheet = client.open("TESTAPI").sheet1

sheet_index=1

with open('list','r') as fd:
    for line in fd.readlines():
        sheet.update_cell(sheet_index, 1, line.decode('utf-8'))
        sheet_index = sheet_index + 1

