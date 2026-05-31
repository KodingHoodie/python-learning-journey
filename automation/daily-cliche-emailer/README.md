# Daily Cliche Emailer

A Python script that reads a list of business clichés from a text file, picks one at random, and sends it as an email using Gmail's SMTP server.

## What It Does

- Reads clichés from a local text file
- Selects one at random
- Sends it as a formatted email using SMTP and MIME

## What I Learned

- Setting up SMTP connection with Gmail
- Building emails with MIMEMultipart and MIMEText
- Reading from a text file and selecting random content
- Securing credentials with environment variables and .env

## How to Run

1. Clone the repo
2. Create a .env file with your Gmail app password: EMAIL_PASSWORD=your_app_password_here
3. Run the script: python send_email.py

## Note

The .env file is not included in this repository for security reasons.

## Course

ZTM Python Automation Bootcamp