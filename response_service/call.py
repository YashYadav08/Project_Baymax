import os
from twilio.rest import Client
from dotenv import load_dotenv


def call(to_number,message):

    # Your Account Sid and Auth Token from twilio.com/console
    
    load_dotenv()
    ACCOUNT_SID = os.getenv("ACCOUNT_SID")      # Get the API token from the .env file.
    AUTH_TOKEN = os.getenv("AUTH_TOKEN")
    
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                            twiml='<Response><Say>'+message+'</Say></Response>',
                            to='+919777662802',
                            from_='+918547885251'
                        )


if __name__=="__main__":
    message = "Hello"
    to_number = "+919057014880"
    call(to_number,message)