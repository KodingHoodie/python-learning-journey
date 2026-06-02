# BrunoBot
A Python chatbot that simulates a conversation with Bruno, a demanding but fair manager at Keiko Corporation. Built using the OpenAI API, this chatbot maintains Bruno’s blunt communication style and dry sense of humor throughout the conversation.

## What It Does
- Prompts the user to ask Bruno an initial question  
- Applies Bruno’s persona using the developer role  
- Keeps responses limited to a single paragraph  
- Maintains conversation history for natural back‑and‑forth  
- Continues the chat until the user types “thanks”  
- Simulates a realistic workplace-style manager interaction  

## What I Learned
- Using the OpenAI chat completions endpoint  
- Setting a fixed persona using the developer role  
- Managing conversation history with a messages list  
- Building a clean conversational loop in Python  
- Handling exit logic with `.strip().lower()`  
- Structuring a project with environment variables and a `.env` file  

## How to Run
1. Clone the repo  
2. Create a `.env` file with your OpenAI API key:  
   ```
   OPEN_AI_KEY=your_api_key_here
   ```
3. Run the script:  
   ```
   python bruno_bot.py
   ```

## Note
The `.env` file is not included in this repository for security reasons.  
Requires an OpenAI API key with available credits.

## Course
ZTM Python Automation Bootcamp