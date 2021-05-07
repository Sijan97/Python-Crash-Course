"""
Python Crash Course
By Eric Matthes

Exercises: 10-11 to 10-13
"""

# Exercise 10-11
# Favorite number
import json

def store_number():
    """Prompts user for their favorite number."""
    favorite_num = input("What is your favorite number? ")
    filename = 'favorite_num.json'

    with open(filename, 'w') as f:
        json.dump(int(favorite_num), f)

    return favorite_num

def get_number():
    """Prints message with favorite number."""
    filename = 'favorite_num.json'

    try:
        with open(filename) as f:
            favorite_num = json.load(f)
    except FileNotFoundError:
        favorite_num = store_number()
    else:
        print(f"I know your favorite number! It's {favorite_num}!")

get_number()

# End of exercise 10-11

# Exercise 10-12
# Favorite number remembered
def favorite_number():
    """Prints the favorite number if available."""
    filename = 'fav_number.json'

    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        favorite_number = input("What is your favorite number? ")
        with open(filename, 'w') as f:
            json.dump(int(favorite_number), f)
    else:
        print(f"I know your favorite number! It's {favorite_number}!") 

# End of exercise 10-12

# Exercise 10-13
# Verify User
def get_new_user():
    """Creates new file with username."""
    username = input("What is your name? ")
    filename = 'user.json'

    with open(filename, 'w') as f:
        json.dump(username, f)

        print(f"We'll remember you when you come back, {username}.")

    return username

def get_user():
    """Retrieves username if available."""
    filename = 'user.json'

    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    """Greets the user by name."""
    username = get_user()

    if username:
        response = input(f"Are you {username} (yes/no)? ")
        if response == 'yes':
            print(f"Welcome back, {username}")
        # else:
        #     username = get_new_user()
        return  # Closes the program if the statement is false.
    else:
        username = get_new_user()

# username = get_new_user() # In case username is wrong.

# End of exercise 10-13