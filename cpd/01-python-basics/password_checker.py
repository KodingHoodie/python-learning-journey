# CPD Course Exercise: Basic Password Checker
# Demonstrates input(), len(), string multiplication, and f-strings.

username = input('What is your username?: ')
password = input('Enter password: ')
password_length = len(password)
hidden_password = '*' * password_length
print(f"{username}, your password, {hidden_password}, is {password_length} letters long.")