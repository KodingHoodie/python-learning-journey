# - Scrimba Exercise: User Input - Exercise
# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# === My Solution for the Challenge ===== #
print("=== User Input Exercise ===")
print()

# Input information:
runner = input("Runner's first name:")
runner = runner.capitalize()
km_distance = float(input("Runner's distance in KM:"))
print()

# Calculations:
km_per_mile = 1.609
convertion = km_distance / km_per_mile 
print()

# Print Statement:
print(f"- Hello {runner}, you ran {km_distance} kilometers. That is {convertion:.2f} converted to miles!")
print()
print("Solid Work! 💯 Good job!")