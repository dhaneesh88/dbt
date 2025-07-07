import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(subject: str, message: str):
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["EMAIL_TO"]
    print("this is mail")
    print(os.environ["EMAIL_USER"])
    print(os.environ["EMAIL_PASSWORD"])
    try:
        with smtplib.SMTP(os.environ["EMAIL_HOST"], int(os.environ["EMAIL_PORT"])) as server:
            server.starttls()
            server.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASSWORD"])
            server.send_message(msg)
        print(f"📧 Email sent: {subject}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")