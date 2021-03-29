import smtplib
import ssl
import os
from dotenv import load_dotenv


def transfer(content, password):
    load_dotenv()
    SENDER = os.environ.get("SENDER_EMAIL")
    RECEIVER = os.environ.get("RECEIVER_EMAIL")

    port = 465
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(SENDER, password)
        server.sendmail(SENDER, RECEIVER, content)
