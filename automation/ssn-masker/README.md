# SSN Masker 

Automation script that detects and partially masks Social Security 
Numbers in a block of text using Regular Expressions.

## What It Does
- Scans a string of text for valid SSN patterns (format: XXX-XX-XXXX)
- Masks the first two segments while keeping the last 4 digits visible
- Converts format from 321-54-9876 to ***-**-9876
- Ignores invalid SSN formats like 321-54 automatically

## What I Learned
- Writing regex patterns with digit quantifiers
- Using capture groups with parentheses
- Using re.sub() to find and replace patterns in text
- Using backreferences to preserve part of the matched pattern

## Course
ZTM Python Automation Bootcamp