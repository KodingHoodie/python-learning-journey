# Tech Trivia Fetcher

A Python script that generates a CSV file of technology trivia questions and answers
fetched from the Open Trivia Database API based on user preferences.

## What It Does

- Asks the user for the number of questions and difficulty level
- Fetches technology trivia from the Open Trivia Database API
- Cleans up HTML entities for readable output
- Flags True or False questions with a clear prefix
- Outputs a structured CSV file with Question and Answer columns

## What I Learned

- Making API requests with the requests library
- Passing parameters to API endpoints
- Parsing JSON responses
- Cleaning HTML entities with the html module
- Writing structured data to a CSV file with user driven input

## How to Run

1. Clone the repo
2. Install dependencies: pip3 install requests
3. Run the script: python trivia_fetcher.py
4. Follow the prompts to enter number of questions and difficulty level
5. A file called tech trivia.csv will be generated in the project folder

## Note

No API key required. This project uses the Open Trivia Database which is free and public.

## Course

ZTM Python Automation Bootcamp