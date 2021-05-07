"""
Python Crash Course
By Eric Matthes

Tutorial: Importing classes 
"""

"""A class that can be used to represent a car."""
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