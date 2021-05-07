"""Python Crash Course
By Eric Matthes

Tutorial: User input
"""

#input() is used to take input from user.
message = input("Tell me something and I will repeat it back: ")
print(message)

#Note: Sublime text don't run programs that prompt the user for input.
#For such programs, terminal is userful.

#multi-line prompt
prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your name? "

name = input(prompt)
print(f"Hello, {name}!")

#Note: += lets the program to write multi-line message to variable.

#Numerical input
age = input("\nHow old are you? ")
int(age)
print(age)

"""Note: The input is string in default, so integer conversion is necessary
to perform numerical operations in the user input."""

#Rollercoster
height = input("\nHow tall are you, in inches? ")
height = int(height)

if height >= 48:
    print(f"You are eligble for the ride!")
else:
    print("You are not tall enough for the ride.")

#Modulo operator

#% or modulo operator returns remainder between two numbers

#Odd or even
number = input("\nEnter a number: ")
number = int(number)

if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is odd number.")