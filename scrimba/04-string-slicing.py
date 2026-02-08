# Scrimba Challenge: Exercise - Strings - Basics/Slicing.
# 1. From the string "Welcome to Python 101: Strings", extract text and create/print new string that says "1 Welcome Ring To Tyler"
# Every first letter in a word should be capitalized(title format)
# Print the same string backwards



# My Solution to the challenge 

msg='welcome to Python 101: Strings'
  
new_msg = msg[18] + " " + msg[0:7] + " " + msg[25:29] + " " + msg[8:10] + " " + (msg[8] + msg[12] + msg[2] + msg[6] + msg[25])

print(new_msg.title())
print(msg[::-1])