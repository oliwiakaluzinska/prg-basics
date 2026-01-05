import re

# read username and password from keyboard
username = input('Enter the username: ')
password = input('Enter the password: ')

# pattern (criteria) for username and password
username_pattern = r'[a-z]{6,}'
password_pattern = r'[A-Za-z0-9_]{8,}'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if password_match and username_match:
   print("Correct!")
else:
   print('Incorrect')