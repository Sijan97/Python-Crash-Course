"""Python Crash Course
By Eric Matthes

Tutorial: functions
"""
# greeter
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

# Calling the function to display greeting
greet_user()

# Passing information to a function
def greet_user(name):
    """Display a simple greeting"""
    print(f"Hello, {name.title()}!")

greet_user('sijan')