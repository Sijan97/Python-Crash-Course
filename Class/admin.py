"""
Python Crash Course
By Eric Matthes

Importing exercise
"""

# Exercise 9-12
from user import User

class Privileges():
    """Describes privileges of admin user."""
    def __init__(self):
        """Initializing attribute."""
        self.privileges = []

    def show_privileges(self):
        """Displays admin privileges."""
        print("\nHere are some admin privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege.title()}")
        else:
            print("- No privileges specified.")


class Admin(User):
    """Describes admin user privileges."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initializing child and parent class attributes."""
        super().__init__(first_name, last_name, username, email, location)
        self.privileges = Privileges()

# See admin_proof.py module for result