"""
Python Crash Course
By Eric Matthes

Tutorial: Importing classes
"""

# my_car.py
from car import Car
# Note: first 'car' represents module and second 'Car' represent class.

my_car = Car('audi', 'v4', 2020)
print(my_car.get_descriptive_name())

my_car.read_odometer()
my_car.update_mileage(45)

my_car.read_odometer()

"""
Multiple classes can be stored in a same module.
But all the classes must be related to each other.

For example, in module tutorial_3, all classes are related to cars.
So, we can create a new file called my_electric_car.py and import 
the ElectricCar class.
"""

#my_electric_class.py
from tutorial_3 import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2020)

print("")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Continue at tutorial_5