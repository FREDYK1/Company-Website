import smtplib
import ssl
import os

def email_send(message, receiver, sender=None):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    sender = sender or username
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(username, password)
            server.sendmail(sender, receiver, message)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")