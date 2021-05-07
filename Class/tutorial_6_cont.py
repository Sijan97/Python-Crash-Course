"""
Python Crash Course
By Eric Matthes

Continued tutorial: tutorial_6
"""

# In this module we import from 2 different modules
from car import Car
from tutorial_6 import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2021)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model x', 2021)
print(my_tesla.get_descriptive_name())

""" 
Using alias:
from tutorial_6 import ElectricCar as EC
"""