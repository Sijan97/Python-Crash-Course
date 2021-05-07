"""
Python Crash Course
By Eric Matthes

Importing exercise
"""

# Exercise 9-12
# user.py
class User:
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initializing the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Summarizing the user profile."""
        summary = f"{self.first_name} {self.last_name}"
        summary += f"\n\tUsername: {self.username}"
        summary += f"\n\tE-mail: {self.email}"
        summary += f"\n\tLocation: {self.location}"

        print(f"\n{summary}")

    def greet_user(self):
        """Greeting the user."""
        greet = f"Welcome back, {self.username}!"
        print(f"\n{greet}")

# Continued module admin.py