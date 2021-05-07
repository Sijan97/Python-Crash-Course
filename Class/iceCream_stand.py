"""Python Crash Course
By Eric Matthes

Exercises: 9-6 to 9-9"""

# Exercise 9-6
# Ice Cream Stand
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


class IceCreamStand(Restaurant):
    """Create a model of ice cream stand and display flavors."""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initializing class attributes."""
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def display_flavors(self):
        """Displays ice cream flavors."""
        print(f"\nAvailable flavors:")
        for count, flavor in enumerate(self.flavors, start=1):
            print(f"{count}. {flavor.title()}")

iceCream = IceCreamStand('BR')
iceCream.flavors = ['chocolate', 'vanilla', 'cotton candy', 'strawberry']

iceCream.describe_restaurant()
iceCream.display_flavors()

# End of exercise 9-6

# Exercise 9-7
# Admin
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

    # def show_privileges(self):
    #     """Displays admin privileges."""
    #     print("\nHere are some admin privileges:")

    #     for privilege in self.privileges:
    #         print(f"- {privilege.title()}")

    # Note: Commented for exercise 9-8.

admin = Admin('sijan', 'shrestha', 'sijan97', 'sijan@example.com', 'kathmandu')

admin.describe_user()
admin.privileges.show_privileges()

print("\nAdding privileges...")

admin_privileges = ['can add post', 'can delete post', 'can ban users']
admin.privileges.privileges = admin_privileges
admin.privileges.show_privileges()

# End of exercise 9-7 and exercise 9-8

# Exercise 9-9
# Battery Upgrade
class Car:
    """A simple representation of a car."""
    def __init__(self, manufacturer, model, year):
        """Initializing the class."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        # self.odometer_reading = 0   # Constantly changing attribute.
        self.odometer_reading = 23  # Modified value.

    def get_descriptive_name(self):
        """Printing a well formatted car detail."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Printing car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_mileage(self, mileage):
        """Updates the mileage of car.
        Rejects change if attempt is made to roll back the odometer.
        """   
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Adds specified value to the odometer.
        Rejects negative increment.
        """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Negative increment detected!")

    def gas_reminder(self):
        """Reminds to fill gas tank."""
        print("Fill in the gas tank as soon as possible.")


# Instance as Attributes
# Making battery a seperate class
class Battery:
    """A simple attempt to model a battery for electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a statement describing the battery."""
        print(f"\nThis car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Prints a statement about the range of the battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"\nThis car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrades the battery size."""
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"\nBattery upgraded to {self.battery_size}-kWh!")
        else:
            print("\nBattery already upgraded!")


class ElectricCar(Car):
    """Represents aspects of a car, specific to electric car."""
    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of parent class.
        Intilialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

    def gas_reminder(self):
        """
        Reminds to fill gas tank.
        Overriding the parent method.
        """
        print("This model does not require gas.")


my_tesla = ElectricCar('Tesla', 'model x', 2020)
my_tesla.battery.battery_size = 75

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

# End of exercise 9-9