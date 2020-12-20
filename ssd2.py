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
print("OK")

ss = sheets.to_json()
print(type(ss))
time.sleep(2)
print(ss)
print("now")
