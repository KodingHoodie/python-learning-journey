from dotenv import dotenv_values
from openai import OpenAI

# ---------------------------------------------------------
# Load API key from .env
# ---------------------------------------------------------
env_vars = dotenv_values('.env')
client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

# ---------------------------------------------------------
# Initial user question + formatting instruction
# ---------------------------------------------------------
initial_prompt = input("Ask Bruno a question!\n")
initial_prompt += " Please limit the response to a single paragraph."

# ---------------------------------------------------------
# Conversation history with Bruno's persona
# ---------------------------------------------------------
messages = [
    {
        "role": "developer",
        "content": [
            {
                "type": "text",
                "text": (
                    "You are Bruno, a manager at the technology firm 'Keiko Corporation' "
                    "with many years of experience. You are a demanding but fair leader, "
                    "with a blunt communication style and a dry sense of humor. "
                    "Respond exactly as Bruno would."
                )
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": initial_prompt
            }
        ]
    }
]

# ---------------------------------------------------------
# Main chat loop — ends when user types "thanks"
# ---------------------------------------------------------
while True:
    # Send full conversation to the model
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=messages
    )

    # Extract Bruno's reply
    content = response.choices[0].message.content
    print(f"{content}\n")

    # Add Bruno's reply to history
    messages.append({"role": "assistant", "content": content})

    # Get next user message
    reply_prompt = input('Respond to Bruno (or type "thanks" to exit):\n')

    # Exit logic (case-insensitive + trims spaces)
    if reply_prompt.strip().lower() == "thanks":
        break

    # Add user message to history
    messages.append({"role": "user", "content": reply_prompt})
