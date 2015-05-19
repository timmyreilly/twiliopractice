#this is for the tokens!
from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "ACc8d230b51fdc71c234e2935f578d09e6" 
AUTH_TOKEN = "fc52be92a5bc7255bf17077b007d2019" 

def get_account_sid():
	return ACCOUNT_SID
	
def get_auth_token():
	return AUTH_TOKEN