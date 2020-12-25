import smartsheet
import requests

# Initialize client
access_token = 'qkxytqvgpu7qu0ujitlpwc32j1'
ss_client = smartsheet.Smartsheet(access_token)

# Make sure we don't miss any errors
ss_client.errors_as_exceptions(True)

print("WELCOME")

sheet_name = "ABHA DAILY REPOT"

def get_the_sheet(ss_client, ss_name):
  search_results = ss_client.Search.search(ss_name).results
  sheet_id = next(result.object_id for result in search_results if result.object_type == 'sheet')
  sheet = ss_client.Sheets.get_sheet(sheet_id)
  return sheet

the_sheet = get_the_sheet(ss_client, sheet_name)

def get_msg_data(sheet):
  msg_data = {}
  the_rows = sheet.rows
  the_row_count = sheet.total_row_count

  wks_col_title ="WORK DONE"
  dt_col_title ="DATE"

  wks_col = sheet.get_column_by_title(wks_col_title)
  dt_col = sheet.get_column_by_title(dt_col_title)

  for n in range(the_row_count):
    the_row = the_rows[n]
    the_wks_col = the_row.get_column(wks_col.id)
    the_dt_col = the_row.get_column(dt_col.id)
    if(the_dt_col.value == "2013-09-19"):
      msg_data['msg']=the_wks_col.value
      msg_data['date']=the_dt_col.value
      return msg_data

the_no = '917028775879'
the_msg = get_msg_data(the_sheet)
only_msg = the_msg['msg']
print(the_msg)

def send_whatsapp_msg(mobile_no, whatsapp_msg):
  headers = {
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    'apikey': '8jto5uzk3utwsrlhjkokftlrrkjtkkfb',
    'cache-control': 'no-cache',
  }

  data = {
  'channel': 'whatsapp',
  'source': '917834811114',
  'destination': mobile_no,
  'message': '{"type":"text","text":"'+whatsapp_msg+'"}',
  'src.name': 'GSDJDDLJ'
  }

  response = requests.post('https://api.gupshup.io/sm/api/v1/msg', headers=headers, data=data)

  print(response)
  print("SENT")

send_whatsapp_msg(the_no, only_msg)

print("THE END")
