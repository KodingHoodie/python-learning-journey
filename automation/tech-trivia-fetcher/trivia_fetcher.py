import requests
import html
import csv

# Base API endpoint
url = "https://opentdb.com/api.php"

# User inputs
amount = input("Please enter the number of trivia questions you'd like to see: ")
difficulty = input("Please specify how difficult you'd like the question to be (easy/medium/hard): ")

# Request parameters
request_params = {
    "amount": amount,
    "difficulty": difficulty,
    "category": "18"
}

# Send API request
response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params=request_params
)

# Extract results
data = response.json()["results"]

# Prepare CSV header
qna = [["Question", "Answer"]]

# Build question/answer rows
for item in data:
    q = html.unescape(item["question"])

    # Add prefix for boolean questions
    if item["type"] == "boolean":
        q = "True or False? " + q

    a = html.unescape(item["correct_answer"])
    qna.append([q, a])

# Write to CSV file
with open("tech trivia.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(qna)