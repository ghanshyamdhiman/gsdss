import smartsheet
import time
import json

# Initialize client
access_token = 'qkxytqvgpu7qu0ujitlpwc32j1'
smartsheet_client = smartsheet.Smartsheet(access_token)

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

response = smartsheet_client.Sheets.list_sheets(include="attachments,source", include_all=True)
sheets = response.data
time.sleep(2)
print(type(sheets))

time.sleep(2)
print(sheets)
print("OK")

for x in range(5):
  print(sheets[x].name)
  print(sheets[x].id)
  
  sname = sheets[x].name
  if(sname == "Ajay Malik"):
    print("\t hello")
    id = sheets[x].id
    sht = sheets[x]
    rs = sht.get_rows()
    time.sleep(2)
    #print(type(rs))
    print(rs)
    r = rs.rows
    print(type(r))
    print(r)
    for s in rs:
      print(s)
    time.sleep(2)
    #print_data(sht,rid)
  time.sleep(3)

def print_data(sheet, row_id):
  row_data = sheet.get_row(row_id)
  print(type(row_data))
"""
for s in sheets:
  print(type(s))
  print(s)
  time.sleep(2)
  print(type(s.name))
  print(s.name)
  time.sleep(2)
"""

print("now")
