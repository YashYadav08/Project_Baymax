import os
from twilio.rest import Client
from dotenv import load_dotenv

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

load_dotenv()
ACCOUNT_SID = os.getenv("ACCOUNT_SID")      # Get the API token from the .env file.
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Hello</Say></Response>',
                        to='+919057014880',
                        from_='+918547885251'
                    )

#print(call.sid)
