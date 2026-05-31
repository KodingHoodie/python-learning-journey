import os
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variable from .env
load_dotenv()

# Credentials
password = os.getenv('EMAIL_PASSWORD')
sender_email = 'jv.crm.sandbox@gmail.com'
receiver_email = 'jv.crm.sandbox@gmail.com'

# Email subject
subject = 'Daily Dose of Inspiration'

# Create MIME message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = sender_email
message['Subject'] = subject

# Load cliches from text file
with open('Business Cliches.txt') as file:
    cliches = file.readlines()

# Pick a random cliche
body = random.choice(cliches)

# Attach body to email
message.attach(MIMEText(body, 'plain'))
message_string = message.as_string()

# Send email
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=receiver_email,
        msg=message_string
    )
