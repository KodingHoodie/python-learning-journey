# Instructions: You are given a list of friends and a new friend to add.

# 1. Add the new friend to the existing list
# 2. Fix the code so that it prints a sorted list of all friends (alphabetical)
# 3. Remember: .sort() returns None, so you cannot print(friends.sort())
# 4. Use the correct method to return a sorted version of the list

# Solution #

friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
new_friend = ['Stanley']

# Add the new friend to the list
friends.extend(new_friend)

# Print a sorted version of the list (sorted() returns a new list
print(sorted(friends))