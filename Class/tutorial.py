"""Python Crash Course
By Eric Matthes

Tutorial: Classes"""

# Creating and using classes
# Creating the dog class

class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        """Simulate a dog rolling over."""
        print(f"{self.name} just rolled over!")

# Making an instance from a class
my_dog = Dog('pintu', 6)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")

# Calling methods
my_dog.sit()
my_dog.roll_over()

# Creating multiple instances
your_dog = Dog('Willie', 7)
another_dog = Dog('Lucy', 5)

print(f"\nYour dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

print(f"\nThere is another dog named {another_dog.name.title()}.")
print(f"Another dog is {another_dog.age} years old.")
another_dog.sit()
another_dog.roll_over()