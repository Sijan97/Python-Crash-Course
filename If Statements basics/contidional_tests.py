"""Python Crash Course
By Eric Matthes

Exercises: 5-1 and 5-2
"""

#Exercise 5-1

car = 'subaru'

print("Is car == 'subaru'? I predict true.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict false.")
print(car == 'audi')

age = 18

print("\nIs age == 18? I predict true.")
print(age == 18)
print("\nIs age ==21? I predict false.")
print(age == 21)

#End of exercise 5-1

#Exercise 5-2

name = 'Dean'

#Conditional test
print(f"\nAll lower case result: {name == 'dean'}")
print(f"\nSame case result: {name == 'Dean'}")
print(f"\nIgnoring case: {name.lower() == 'dean'}")
print(f"\nInequaliy case: {name != 'dean'}")
print(f"\nInequaliy case in correct case: {name != 'Dean'}")

#If statements
if name == 'Dean':
    print(f"\nHello, {name}!")

if name != 'dean':
    print(f"\nHello, {name}!")

if name != 'Dean':
    print("Statement closed! Won't print anything.")
print(f"\nAbove statement test result: {name != 'Dean'}")

if name.lower() == 'dean':
    print(f"\nHello, {name}!")

if name.lower() != 'dean':
    print(f"\nHello, {name}!")
print(f"\nAbove statement test result: {name.lower() != 'dean'}")

#Numerical tests
age = 18
print(f"Equality test: {age == 18}")
print(f"Inequality test: {age != 21}")
print(f"Greater than test: {age > 5}")
print(f"Less than test: {age < 21}")
print(f"Multiple cases test: {age > 18 and age <= 52}")
print(f"Another multiple cases test: {age > 18 or age <= 52}")

#Test if an item is in a list
cars = ['bmw', 'subaru', 'toyota', 'volkswagen']
print(f"Checking if item is in the list: {'bmw' in cars}")
print(f"Checking if item is not in the list: {'skoda' not in cars}")

#End of exercise 5-2