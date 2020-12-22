import smartsheet
import time
import json
import os
from twilio.rest import Client

# Initialize client
access_token = 'qkxytqvgpu7qu0ujitlpwc32j1'
smartsheet_client = smartsheet.Smartsheet(access_token)

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

response = smartsheet_client.Sheets.list_sheets(include="attachments,source", include_all=True)
sheets = response.data
print('Prog Starts')
print(type(sheets))
time.sleep(2)
print("OK")

for x in range(1):
  print(sheets[x].name)
  print(sheets[x].id)
  s_id = sheets[x].id
  sht = sheets[x]
  cols = sht.get_columns(s_id)
  cols_json = cols.to_json()
  print(type(cols_json))
  print(cols_json)
  time.sleep(3)
  cols_data = json.loads(cols_json)
  print(type(cols_data))
  print(cols_data)
  time.sleep(3)
  #print(cols_json['id]'])
  cols_count = cols.total_count
  for d in cols_data:
    print(d)
    
  for d in cols_data.values():
    print(type(d))
    print(d)
    for i in d:
      print(type(i))
      print(i)
      for x, y in i.items():
        print(x, y)
        time.sleep(2)

    time.sleep(2)

  

  print("now")
