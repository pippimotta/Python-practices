from twilio.rest import Client

TWILIO_SID = 'ACc79a007535e78fa3cfa8fcf32771d394'
TWILIO_AUTH_TOKEN = '3dfe9c7f58405f56ef57617eeb63ba3c'
TWILIO_VIRTUAL_NUMBER = '+18647079285'
TWILIO_VERIFIED_NUMBER = '+817018127929'



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
