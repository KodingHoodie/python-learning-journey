# CPD Course Exercise: Tricky Counter
# INSTRUCTIONS:
# Write a program that calculates the sum of all numbers in the list.
# This exercise practices:
# - for loops
# - the accumulator pattern (adding to a running total)
# - iterating through lists


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0

for item in my_list:
    counter += item

print(counter)