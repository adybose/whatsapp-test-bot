from twilio.rest import Client
import constants

# client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
# DANGER! This is insecure. See http://twil.io/secure
client = Client(constants.account_sid, constants.auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number = constants.from_whatsapp_number
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number = constants.to_whatsapp_number

message = client.messages.create(body='Hello, World!',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

print(message)
