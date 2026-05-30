## Diff Analyzer

Automation script that compares two ranges of cells across two worksheets in an Excel spreadsheet and outputs a summary of all differences into a new worksheet.

## What It Does

- Prompts the user to specify two worksheet names and their corresponding cell ranges
- Validates that both ranges have identical dimensions before proceeding
- Compares each cell pair row by row and column by column
- Records every difference found including the row number, column header, and both values
- Creates a new worksheet called Diffs and writes all differences with headers
- Writes a delta formula for rows where both values are numeric showing the percentage difference
- Formats the delta column in red with percentage formatting

## What I Learned

- Loading and saving Excel workbooks with openpyxl
- Navigating and comparing cell ranges across multiple worksheets
- Collecting and structuring data differences into a list of lists
- Dynamically writing data and formulas to a new worksheet
- Applying font color and number formatting with openpyxl styles

## Course
ZTM Python Automation Bootcamp