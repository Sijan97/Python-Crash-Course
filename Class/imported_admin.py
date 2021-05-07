"""
Python Crash Course
By Eric Matthes

Import exercise
"""

# Exercise 9-11
# Imported Admin
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


# Exercise 9-8
# Privileges
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

# Continued in module proofs.py