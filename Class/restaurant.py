"""Python Crash Course 
By Eric Matthes

Exercises: 9-1 to 9-3"""

# Exercise 9-1
# Restaurant
class Restaurant:
    """Describing a restaurant and opening it."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing restaurant name and cuisine type attributes."""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        """Giving a plain description of the restaurant."""
        print(f"Welcome to {self.name.title()}!")
        print(f"Help yourself with our delicious {self.cuisine} delicacy.")

    def open_restaurant(self):
        """Printing a message indicating that the restaurant is open."""
        print(f"{self.name.title()} is now open!")

# Making an instance from class Restaurant
restaurant = Restaurant('casa mexicana', 'mexican')

print(f"Our restaurant is called {restaurant.name.title()}.")
print(f"We provide authentic {restaurant.cuisine} dishes.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

# End of exercise 9-1

# Exercise 9-2
# Three restaurants
# Creating three different instances from class Restaurant
pizza_hut = Restaurant('pizza hut', 'pizza')
momo_restaurant = Restaurant('bota', 'momo')
stick_food = Restaurant('chinese garden', 'chinese')

# Calling method describe_restaurant() from class Restaurant
print("")
pizza_hut.describe_restaurant()

print("")
momo_restaurant.describe_restaurant()

print("")
stick_food.describe_restaurant()

# End of exercise 9-2

# Exercise 9-3
# Users
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

# Creating instances from class User
user = User('sijan', 'shrestha', 'sijan97', 'sid.fire9z@gmail.com', 'nepal')
user_2 = User('eric', 'matthes', 'ematt', 'eric.matthes@gmail.com', 'america')
user_3 = User('phil', 'collins', 'pcoll', 'phil.collins@gmail.com', 'England')

# Calling methods
user.describe_user()
user.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()

# End of exercise 9-3