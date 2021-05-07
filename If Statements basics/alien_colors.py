"""Python Crash Course
By Eric Matthes

Exercises: 5-3 to 5-7

"""

#Exercise 5-3

alien_color = 'Green'

#Testing successful if statement
if alien_color.lower() == 'green':
    print("You just earned 5 points!")

#Testing failure if statement
if alien_color.lower() == 'blue':
    print("nothing")

#End of exercise 5-3

#Exercise 5-4

alien_color1 = 'green'

#If block runs:
if alien_color1.lower() == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#Else block runs:
alien_color2 = 'red'

if alien_color2 == 'green':
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#End of exercise 5-4

#Exercise 5-5
alien_color3 = 'red'

if alien_color3 == 'green':
    print("You just earned 5 points!")
elif alien_color3 == 'yellow':
    print("You just earned 10 points!")
else:
    print("You just earned 15 points!")

#End of exercise 5-5

#Exercise 5-6
age = 18

if age < 2:
    print("You're a baby!")
elif age >= 2 and age < 4:
    print("You're a toddler!")
elif age >= 4 and age < 13:
    print("You're a kid!")
elif age >= 13 and age < 20:
    print("You're a teenager!")
elif age >= 20 and age < 65:
    print("You're an adult!")
else:
    print("You're an elder!")

#End of exercise 5-6

#Exercise 5-7
favorite_fruits = ['apple', 'mango', 'banana']

if 'apple' in favorite_fruits:
    print("You really like apple!")

if 'mango' in favorite_fruits:
    print("You really like mango!")

if 'banana' in favorite_fruits:
    print("You really like banana!")  

if 'cherry' in favorite_fruits:
    print("You really like cherry!")

if 'avocado' in favorite_fruits:
    print("You really like avocado!")

#End of exercise 5-7