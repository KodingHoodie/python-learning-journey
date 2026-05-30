# Clean Sweeper Project

Automation script that organizes a messy directory by sorting 
files and folders into categorized sub-directories automatically.

## What It Does
Asks the user for a directory path, then automatically:
- Creates a "closet" folder with sub-folders for text files, 
  CSV files, and folders
- Moves all .txt files into the text_files sub-folder
- Moves all .csv files into the csv_files sub-folder
- Deletes any folders with "temp" in the name
- Moves all remaining folders into the folders sub-folder
- Moves any remaining files directly into closet
- Prints "Folder cleanup complete!" when done

## What I Learned
- Navigating file systems with Pathlib
- Creating directories with mkdir()
- Iterating over files and folders with iterdir()
- Moving files with shutil.move()
- Deleting folders with shutil.rmtree()
- Using if/elif/else conditions strategically

## Course
ZTM Python Automation Bootcamp