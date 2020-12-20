import smartsheet
import time
import json

# Initialize client
access_token = 'qkxytqvgpu7qu0ujitlpwc32j1'
smartsheet_client = smartsheet.Smartsheet(access_token)

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

"""
response = smartsheet_client.Sheets.list_sheets(include="attachments,source", include_all=True)
sheets = response.data
"""

response = smartsheet_client.Favorites.list_favorites(include_all=True)
print(type(response))
print("OK")
faves = response.data
print(type(faves))
print(faves)
ss = response.to_json()
print(type(ss))
print(ss)
gs = json.dumps(ss)
print(gs[1].objectId)
print("now")
"""
for x in range(5):
  print(ss[1][1])
  time.sleep(1)

"""