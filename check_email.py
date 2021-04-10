import os
from dotenv import load_dotenv


def check_email():
    load_dotenv()
    SENDER = os.environ.get("SENDER_EMAIL")
    RECEIVER = os.environ.get("RECEIVER_EMAIL")
    return SENDER and RECEIVER
