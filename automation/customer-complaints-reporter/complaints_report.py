from datetime import date
import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Load environment variables
load_dotenv()
sender_email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')

# Load recipient emails
with open('dummy_emails.txt', 'r') as emails_file:
    emails = [email.strip() for email in emails_file.readlines()]

# Email subject
subject = f"Status Report for {date.today()}"

# Create email message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = ', '.join(emails)
message['Subject'] = subject

# Attach complaints file + count complaints
with open('customer_complaints.txt', 'rb') as attachment:
    data = attachment.readlines()
    attachment.seek(0)
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename=customer_complaints.txt')

# Email body
body = f"There are {len(data) - 1} complaints in today's file."
message.attach(MIMEText(body, 'plain'))

# Add attachment
message.attach(part)

# Convert to string
message_string = message.as_string()

# Send email
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=sender_email, password=password)
    connection.sendmail(from_addr=sender_email, to_addrs=emails, msg=message_string)
