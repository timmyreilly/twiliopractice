#Main file
from tokens import *

from twilio.rest import TwilioRestClient

ACCOUNT_SID = get_account_sid()
AUTH_TOKEN = get_auth_token()
TWILIO_NUMBER = get_twilio_number()
MY_PHONE_NUMBER = get_phone_number()

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hey Hey Hey",
    to=MY_PHONE_NUMBER,    # Replace with your phone number
    from_=TWILIO_NUMBER) # Replace with your Twilio number
print message.sid



