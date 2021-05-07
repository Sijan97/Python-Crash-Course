"""
Python Crash Course
By Eric Matthes

Continued tutorial: Importing classes
"""

# Importing a module into a module

"""
In this tutorial we will save ElectricCar class and Battery class in same
module and Car class in seperate module and import Car class from car.py
module to electricCar.py(tutorial_6) module.
"""

from car import Car

class Battery:
    """A simple attempt to model a battery for electric car."""
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Prints a statement describing the battery."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Prints a statement about the range of the battery."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


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


# Continue on another module.