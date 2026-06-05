# Instructions:
# 1. Create a user profile for your new game. This user profile will be stored in a dictionary with keys:
#  'age', 'username', 'weapons', 'is_active', and 'clan'
# 2. Iterate and print all the keys in the above user.
# 3. Add a new weapon to your user.
# 4. Add a new key 'is_banned' and set it to False.
# 5. Ban the user by setting 'is_banned' to True.
# 6. Create a new user2 by copying the previous user and update the age value and username value.

# Solution #

# 1. Create the user profile dictionary
user_profile = {
    'age': 0,
    'username': '',
    'weapons': None,
    'is_active': False,
    'clan': None
}

# 2. Print all keys in the dictionary
print(user_profile.keys())

# 3. Add a new weapon
user_profile['weapons'] = 'AK 47'

# 4. Add a new key 'is_banned' and set it to False
user_profile.update({'is_banned': False})

# 5. Ban the user by setting 'is_banned' to True
user_profile['is_banned'] = True

# 6. Copy the user and update age + username
user2 = user_profile.copy()
user2.update({'age': 47, 'username': 'user2'})

print(user_profile)
print(user2)