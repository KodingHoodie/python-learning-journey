## Diff Analyzer - Google Sheets

Automation script that compares two ranges of cells across two worksheets in a Google Sheets spreadsheet and outputs a summary of all differences into a new worksheet.

## What It Does

- Connects to Google Sheets using a service account credentials file
- Prompts the user to specify two worksheet names and their corresponding cell ranges
- Compares each cell pair row by row and column by column
- Records every difference found including the row number, column header, and both values
- Handles both numeric and text value differences correctly
- Creates a new worksheet called Diffs and writes all differences with headers
- Deletes and recreates the Diffs sheet automatically on repeated runs to avoid duplicates

## What I Learned

- Connecting to the Google Sheets API using gspread and a service account
- Reading cell ranges from Google Sheets with the get() method
- Handling data as strings and converting numeric values with float()
- Understanding how indentation affects logic flow in nested if statements
- Writing data back to Google Sheets with the update() method
- Managing worksheets programmatically by adding and deleting them

## Note

This project requires a Google Cloud service account credentials file to run.
The credentials file is not included in this repository for security reasons.

## Course
ZTM Python Automation Bootcamp