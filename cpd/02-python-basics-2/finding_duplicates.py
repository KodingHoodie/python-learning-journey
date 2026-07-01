# CPD Course Exercise: Find Duplicates
# INSTRUCTIONS:
# Given a list of characters, identify which items appear more than once.
# Print only the characters that have duplicates.

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
