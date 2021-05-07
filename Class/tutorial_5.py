"""
Python Crash Course
By Eric Matthes

Continued tutorial_4
"""

# Importing multiple classes
from tutorial_3 import Car, ElectricCar

my_toyota = Car('toyota', 'land cruiser', 2021)

my_tesla = ElectricCar('tesla', 'model x', 2021)

print(my_toyota.get_descriptive_name())
print(my_tesla.get_descriptive_name())

# Importing an entire module
import tutorial_3

my_beetle = tutorial_3.Car('volkswagen', 'beetle', 2021)

my_new_tesla = tutorial_3.ElectricCar('tesla', 'roadster', 2021)

print("")
print(my_beetle.get_descriptive_name())
print(my_new_tesla.get_descriptive_name())


# Similarly, we can import all classes of a module using the syntax:
# from module_name import *