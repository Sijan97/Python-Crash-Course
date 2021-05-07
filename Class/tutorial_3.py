"""Python Crash Course 
By Eric Matthes

Tutorial: Inheritance"""

# The __init__() method for a child class
# Electric car
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

# my_tesla = ElectricCar('tesla', 'model s', 2020)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.gas_reminder()
# my_tesla.battery.get_range()