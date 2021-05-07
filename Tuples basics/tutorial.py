"""
Python Crash Course 
By Eric Matthes

Tuples Tutorial
Definition: Tuples are basically immutable lists, which means that
the values defined in tuples cannot be changed. Tuples are defined
using parentheses.

"""

#Defining tuple
planets = ('earth', 'mercury', 'jupiter', 'saturn', 'mars')
print(f"We live on planet {planets[0].title()}.")

dimensions = (200,40)
print(f"The width of the rectangle: {dimensions[0]}")

#Trying to modify the tuple
#dimensions[0] = 50 
#Generates TypeError: 'tuple' object does not support item assignment

#Looping through tuple
print("PLanets in our solar system:")
for planet in planets:
    print(planet.title())

print("Dimensions of a rectangle:")
for dimension in dimensions:
    print(dimension)

#Changing the values of tuple
"""
Although tuples are immutable, if the values of tuples needed to be changed, 
the tuple must be redefined.

"""
print(f"Original tuple: {dimensions}")
dimensions = (300,100)  #The tuple 'dimensions' is redefined with new values.
print(f"Modified tuple: {dimensions}")