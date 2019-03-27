import  twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3a081096f50b15e338e7b44f078c4b0f"
# Your Auth Token from twilio.com/console
auth_token  = "3ddd1f5b18a1d9e6008541cabc5fedd7"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918384806706", 
    from_="+12029309812",
    body="Hello from Dev!")

print(message.sid)

