# Customer Complaints Reporter

A Python script that automates the sending of a daily email report about customer complaints.
Reads a list of recipients, counts the complaints in a file, and sends a formatted email
with the complaint file attached.

## What It Does

- Reads recipient email addresses from a local text file
- Counts the number of complaints in the complaints file
- Builds an email with a dynamic subject line using the current date
- Attaches the complaints file to the email
- Sends the report to all recipients using Gmail SMTP with TLS

## What I Learned

- Sending emails to multiple recipients with SMTP
- Attaching files to emails using MIMEBase and encoders
- Reading and counting lines from a text file
- Dynamically generating content using the datetime module
- Securing credentials with environment variables and .env

## How to Run

1. Clone the repo
2. Create a .env file with your Gmail app password: EMAIL_PASSWORD=your_app_password_here
3. Run the script: python complaints_report.py

## Note

The .env file is not included in this repository for security reasons.

## Course

ZTM Python Automation Bootcamp