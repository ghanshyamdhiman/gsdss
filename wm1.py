import requests

the_no = '917028775879'
the_msg ='You have earned [55] points at [RAN]'

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

send_whatsapp_msg(the_no, the_msg)

