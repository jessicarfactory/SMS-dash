import os
from twilio.rest import Client
from dotenv import load_dotenv
import datetime

load_dotenv()

TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
twilio_api = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


def fetch_sms():
    return twilio_api.messages.stream()
    print(twilio_api.messages.stream())

