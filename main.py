#Main file
from tokens import *
from HelperFunctions import *
from azure.storage import QueueService
from twilio.rest import TwilioRestClient

ACCOUNT_SID = get_account_sid()
AUTH_TOKEN = get_auth_token()
TWILIO_NUMBER = get_twilio_number()
MY_PHONE_NUMBER = get_phone_number()

account_name = get_storage_account_name()
account_key = get_storage_account_key()
working_queue = get_working_queue()


def get_queue_string():
    messages = queue_service.get_messages(working_queue)
    for message in messages:
        print(message.message_text)
        queue_service.delete_message(working_queue, message.message_id, message.pop_receipt)
    return str(message.message_text)

queue_service = QueueService(account_name, account_key)

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

message_text = get_state_managed_queue()

message = client.messages.create(
    body=message_text,
    to=MY_PHONE_NUMBER,    # Replace with your phone number
    from_=TWILIO_NUMBER) # Replace with your Twilio number

print message.sid



