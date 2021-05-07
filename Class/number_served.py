"""Python Crash Course
By Eric Matthes

Exercises: 9-4 to 9-5"""

# Exercise 9-4
# Number Served
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

# Number of customers served
restaurant = Restaurant('pizza hut', 'pizza')
# print(f"{restaurant.name} has served {restaurant.number_served} customers.")
restaurant.get_customer_number()

# Changing the number_served attribute directly and printing again
# print(f"\n{restaurant.name} has served {restaurant.number_served} customers.")
restaurant.number_served = 10

print("\nAfter change:")
restaurant.get_customer_number()

# Changing the customer number from method
restaurant.set_number_served(20)
print("\nAfter setting:")
restaurant.get_customer_number()

# Creating new method to increment the customer value
restaurant.increment_number_served(10)
print("\nAfter increment:")
restaurant.get_customer_number()

# End of exercise 9-4

# Exercise 9-5
# Login Attempts
class User:
    """Represent a simple user profile."""
    def __init__(self, first_name, last_name, username, email, location):
        """Initializing the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Summarizing the user profile."""
        full_name = f"{self.first_name} {self.last_name}"
        summary = f"User profile successfully created for {full_name}."
        summary += f"\nUsername for {full_name} is '{self.username}'. "
        summary += f"\nPrimary e-mail for {full_name} is set as {self.email}. "
        summary += f"\n{full_name} currently lives in {self.location}."

        print(f"\n{summary}")

    def greet_user(self):
        """Greeting the user."""
        greet = f"Welcome back, {self.username}!"
        print(f"\n{greet}")

    def increment_login_attempts(self):
        """Sets increments value for login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the number of login attempts to 0."""
        self.login_attempts = 0

# Making instance
user = User('sijan', 'shrestha', 'sijan97', 'sijan@example.com', 'kathmandu')

# Calling increment function
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Printing the number of logins incremented
print(f"\nLogin attempts: {user.login_attempts}")

# Resetting login attempts
user.reset_login_attempts()
print(f"\nLogin attempts: {user.login_attempts}")

# End of exercise 9-5