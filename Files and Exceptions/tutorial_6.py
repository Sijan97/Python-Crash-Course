"""
Python Crash Course
By Eric Matthes

Tutorial: Refactoring
"""

# Definition: Refactoring is breaking the chunk of code into smaller chunks.
# We can achieve this by creating seperate functions for seperate tasks.

# remember_me_3.py
import json

# def greet_user():
#     """Greets the user by name."""
#     filename = 'username.json'

#     try:
#         with open(filename) as f:
#             username = json.load(f)
#     except FileNotFoundError:
#         username = input("What is your name? ")

#         with open(filename, 'w') as f:
#             json.dump(username, f)

#             print(f"We'll remember you when you come back, {username}.")
#     else:
#         print(f"Welcome back, {username}!")

# greet_user()

# The above function does all the tasks by itslelf. So lets refactor it.
# Lets define new function for retrieving file and creating file.
def get_stored_username():
    """Returns the username if available."""
    try:
        filename = 'username.json'

        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def create_new_user():
    """Creates new file for username."""
    username = input("What is your name? ")    
    filename = 'username.json'

    with open(filename, 'w') as f:        
        json.dump(username, f)
    return username

def greet_user():
    """Greets the user by name."""
    username = get_stored_username()

    if username:
        print(f"Welcome back, {username}")
    else:
        username = create_new_user()
        print(f"We'll remember you when you come back, {username}!")

greet_user()