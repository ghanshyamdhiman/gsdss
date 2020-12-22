import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
#TWILIO_ACCOUNT_SID = 'ACa64794fbb24c7f3d3c082a9c41b4ff25'
TWILIO_ACCOUNT_SID= 'SK1a838acbd1c9dd738375c6a653dd7640'
#TWILIO_AUTH_TOKEN= 'ed7c8a864d30310dfa4b4973dceff57c'
TWILIO_AUTH_TOKEN='nRSAMX1X2qAHRfF6dZ5VyRL5LAhhPTRs'
account_sid = os.environ[TWILIO_ACCOUNT_SID]
auth_token = os.environ[TWILIO_AUTH_TOKEN]
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+917028775879',
                              to='whatsapp:+91950357231'
                          )

print(message.sid)