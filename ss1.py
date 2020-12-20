import smartsheet
import time
import json

# Initialize client
access_token = 'qkxytqvgpu7qu0ujitlpwc32j1'
smartsheet_client = smartsheet.Smartsheet(access_token)

# Make sure we don't miss any errors
smartsheet_client.errors_as_exceptions(True)

response = smartsheet_client.Sheets.list_sheets(include_all=True)
sheets = response.data
time.sleep(2)
print(type(sheets))
time.sleep(3)

response = smartsheet_client.Favorites.list_favorites(include_all=True)
print(type(response))
print("OK")
faves = response.data
print(type(faves))
print(faves)
ss = response.to_json()
print(type(ss))
print(ss)
gs = json.loads(ss)
print(type(gs))
print(gs)

for i in enumerate(gs.items()): 
  print(type(i))
  for x in i[1]:
    print(type(x))
    print(x)
    for y in x:
      print(type(y))
      time.sleep(2)
      print(y)
      #c = json.dumps(y)
      for a in y: 
        print(type(a))  
        print(a[0][0])
    time.sleep(1)

print("now")
"""
for x in range(5):
  print(ss[1][1])
  time.sleep(1)

"""