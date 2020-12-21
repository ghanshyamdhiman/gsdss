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
  print(sheets[x].get_rows())
  time.sleep(2)
    #print_data(sht,rid)
  time.sleep(3)

def print_data(sheet, row_id):
  row_data = sheet.get_row(row_id)
  print(type(row_data))

print("now")
