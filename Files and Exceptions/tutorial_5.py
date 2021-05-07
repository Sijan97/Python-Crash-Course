"""
Python Crash Course
By Eric Matthes

Tutorial: JSON files
"""

# Storing and reading user-generated data
# remember_me.py
import json

username = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}.")

# Loading the username
with open(filename) as f:
    user = json.load(f)
    print(f"Welcome back, {user}!")

# remember_me_2.py
# Load the username if it already exists.
# Otherwise, prompt the user to provide a username.
filename = 'username_1.json'

try:
    with open(filename) as f:
        username_1 = json.load(f)
except FileNotFoundError:
    with open(filename, 'w') as f:
        username_1 = input("What is your name? ")
        json.dump(username_1, f)

        print(f"We'll remember you when you come back, {username_1.title()}.")
else:
    print(f"Welcome back, {username_1.title()}")