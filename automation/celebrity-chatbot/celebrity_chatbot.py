from dotenv import dotenv_values
from openai import OpenAI

# Load API key from .env file
env_vars = dotenv_values('.env')
client = OpenAI(api_key=env_vars['OPEN_AI_KEY'])

# Ask the user which celebrity they want to talk to
famous_person = input("What celebrity would you like to talk to?\n")

# First question the user wants to ask the celebrity
initial_prompt = input(f"Ok! Now ask {famous_person} a question!\n")

# Add a small instruction to keep responses short
initial_prompt = (initial_prompt +
                  " Please limit the response to a single paragraph and include soft line breaks for readability.")

# Build the initial conversation history:
# - Developer role sets the persona (the celebrity)
# - User role contains the first question
messages = [
    {
        "role": "developer",
        "content": [
            {
                "type": "text",
                "text": (
                    f"You are {famous_person}. Respond exactly as this person would, "
                    f"staying fully in character."
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

# Main chat loop — continues until the user types "bye"
while True:
    # Send the full conversation history to the model
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=messages
    )

    # Extract the assistant's reply
    content = response.choices[0].message.content

    # Add the assistant's reply to the conversation history
    messages.append({"role": "assistant", "content": content})

    # Display the reply
    print(content)

    # Ask the user for the next message
    prompt = input(f"Respond to {famous_person} (or type 'bye' to exit):\n")

    # Exit the loop if the user is done
    if prompt.strip().lower() == "bye":
        break

    # Add the user's new message to the conversation history
    messages.append({"role": "user", "content": prompt})
