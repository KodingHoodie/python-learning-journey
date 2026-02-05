# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

# 🧠 ==== My Code For The Challenge ==== #

# Customer information:
customer_name = "John Doe"
passes_bought = 2
tokens_per_pass = 45
price_per_pass =  15.55
tokens_per_game = 5

# Calculations: 
total_tokens = passes_bought * tokens_per_pass
total_cost = passes_bought * price_per_pass
games_available = total_tokens // tokens_per_game

# Arcade Pass Summary: 
print("Arcade Pass Summary 📝")
print()
print("* Customer Info *")
print(f"Customer Name: {customer_name}")
print(f"Passes Bought: {passes_bought}")
print()
print("* Calculation Results * ")
print(f"Total tokens: {total_tokens}")
print(f"Total Cost: ${total_cost:.2f}")
print(f"Games Available: {games_available}")
print()
print("Thanks for playing! 🎮 Come back soon!")

# ===== My own variation / extra practice ===
# Trying the multi-line f-string style for a cleaner summary block

summary = f"""
Arcade Pass Summary 📝

Customer Info:
    Customer Name: {customer_name}
    Passes Bought: {passes_bought}

Calculation Results:
    Total Tokens: {total_tokens}
    Total Cost: ${total_cost:.2f}
    Games Available: {games_available}

Thanks for playing! 🎮 Come back soon!
"""

print(summary)