from data.env_vars import TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID, TWILIO_PHONE_NUMBER, TWILIO_TO_NUMBER
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message: str):
        """Sends an SMS with the message indicated"""
        content = self.client.messages.create(to=TWILIO_TO_NUMBER, from_=TWILIO_PHONE_NUMBER,
                                              body=message)
        # print(content.status)
        return content.status
