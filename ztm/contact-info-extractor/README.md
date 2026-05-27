# Contact Info Extractor

Automation script that scans a text file and extracts all phone 
numbers, email addresses, and website addresses into separate 
organized text files using Regular Expressions.

## What It Does
- Reads a plaintext file containing unstructured contact information
- Uses regex patterns to identify phone numbers, emails, and websites
- Removes duplicate matches automatically
- Writes results to three separate output files:
  - phone_numbers.txt
  - emails.txt
  - websites.txt

## What I Learned
- Building complex regex patterns for real world data
- Using re.findall() to extract multiple matches from text
- Processing and deduplicating regex match results
- Writing lists of data to text files with writelines()

## Course
ZTM Python Automation Bootcamp