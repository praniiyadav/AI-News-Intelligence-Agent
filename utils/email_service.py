import os
import smtplib

from email.mime.text import MIMEText

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(receiver_email, topic, summary):

    email_body = f"""
Hello Iam AI News,

Here are the latest news updates about {topic}.

{summary}

Best Regards,
Pranii's AI News Intelligence Agent
"""

    msg = MIMEText(email_body)

    msg["Subject"] = f"🚀 Latest News on {topic}"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    server.sendmail(EMAIL_ADDRESS, receiver_email, msg.as_string())

    server.quit()
