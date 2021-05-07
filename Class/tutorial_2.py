"""Python Crash Course 
By Eric Matthes

Tutorial: Classes and instances"""

# car.py
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

my_car = Car('audi', 'a4', 2020)
print(my_car.get_descriptive_name())
my_car.read_odometer()

# Modifying attribute values
# Modifying directly
# attribute odometer_reading modified directly in class Car
print("")
my_car.read_odometer()

# Modifying through method
# Define new method in class Car to update mileage
my_car.update_mileage(50)

print("")
my_car.read_odometer()

# Trying to roll back odometer
my_car.update_mileage(23)

# Incrementing attributes value through method
# Define new method to increment the odometer in class Car
my_car.increment_odometer(100)
print("")
my_car.read_odometer()

# Attempting negative increment
my_car.increment_odometer(-100)

print("")
my_car.update_mileage(23_500)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()