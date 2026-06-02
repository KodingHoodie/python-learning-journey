# Celebrity Chatbot

A Python chatbot that simulates a conversation with any celebrity or famous person
using the OpenAI API. The user chooses who they want to talk to and how creative
the responses should be.

## What It Does

- Asks the user to choose a celebrity to talk to
- Takes an initial question to kick off the conversation
- Lets the user control the creativity level of responses
- Maintains conversation history for natural back and forth dialogue
- Type "bye" to exit the conversation

## What I Learned

- Making API calls to OpenAI using the chat completions endpoint
- Using the developer role to set a persona for the AI
- Managing conversation history with a messages list
- Taking user input to dynamically control API behavior
- Building a conversational loop in Python

## How to Run

1. Clone the repo
2. Create a .env file with your OpenAI API key: OPEN_AI_KEY=your_api_key_here
3. Run the script: python celebrity_chatbot.py

## Note

The .env file is not included in this repository for security reasons.
Requires an OpenAI API key with available credits.

## Course

ZTM Python Automation Bootcamp