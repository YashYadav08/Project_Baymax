# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC63fbfad00244b74bf760c38113f3788e'
auth_token = 'c7d4c4b0bc186bf467499e69c979b90e'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Hello</Say></Response>',
                        to='+919057014880',
                        from_='+918547885251'
                    )

print(call.sid)
