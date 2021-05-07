"""Python Crash Course
By Eric Matthes

Exercises: 8-1 to 8-2
"""

# Exercise 8-1
# Message
def display_message():
    """Displays chapter information"""
    print("We are learing about functions in this chapter.")

# Calling the function
display_message()

# Exercise 8-2
# Favorite book
def favorite_book(title):
    """Displays title of one of my favorite books"""
    print(f"\nOne of my favorite books is {title.title()}.")

#Calling the function with argument
favorite_book('python crash course')