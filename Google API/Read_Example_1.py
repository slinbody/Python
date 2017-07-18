#!/usr/bin/python
# -*- coding: utf8 -*-
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the Sheets API.

    Creates a Sheets API service object and prints the names and majors of
    students in a sample spreadsheet:
    https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit
    """
    credentials = get_credentials()
    print("get_credentials DONE")
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    spreadsheetid = 'Your_Sheet_ID'
    rangeName = "XXX!C2:H21"
    MajorDimension = 'ROWS'


    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetid, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print('Data Reading:')
        Analysis_Data(values)



def Analysis_Data(Data_from_Google):
    result = [{u'C':0, u'G':0, u'J':0},
              {u'C':0, u'G':0, u'J':0},
              {u'C':0, u'G':0, u'J':0},
              {u'C':0, u'G':0, u'J':0},]

    for row_index, row in enumerate(Data_from_Google):
#        print("row_index Data_from_Google.index: {} {}".format(row_index,Data_from_Google.index(row)))
#        print(row)
        row_index_4 = row_index % 4
        if row_index_4 == 0:
            continue
#        print(result[row_index])
        for i in row:
#            print(i, end=' >')

            if i in result[row_index_4]:
                result[row_index_4][i] = result[row_index_4][i] + 1
#                print(i, end=' _')
#        print('result[{}]: {}'.format(row_index_4,result[row_index_4]))
#        print('-----------')

    print('C  G  J')
    for i in range(1,4):
       for j in [u'C', u'G', u'J']:
           print('{:4d}'.format(result[i][j]),end= ' ')
       print('')

if __name__ == '__main__':
    main()
