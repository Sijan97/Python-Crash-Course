"""
Python Crash Course
By Eric Matthes

Import Exercises
"""

# Exercise 9-10
# restaurant.py
class Restaurant:
    """Describing a restaurant and opening it."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurant name and cuisine type attributes."""
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Giving a plain description of the restaurant."""
        print(f"Welcome to {self.name.title()}!")
        print(f"Help yourself with our delicious {self.cuisine} delicacy.")

    def open_restaurant(self):
        """Printing a message indicating that the restaurant is open."""
        print(f"{self.name.title()} is now open!")

    def get_customer_number(self):
        """Prints number of customers who visited the restaurant."""
        print(f"{self.name} has served {self.number_served} customers.")

    def set_number_served(self, customer_number):
        """Sets number of customer who visited the restaurant."""
        self.number_served = customer_number

    def increment_number_served(self, increment_number):
        """Sets the customer increment number."""
        self.number_served += increment_number

# Continued in module proofs.py