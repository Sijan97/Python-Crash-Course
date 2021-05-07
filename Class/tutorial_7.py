"""
Python Crash Course
By Eric Matthes

Tutorial: Random module
"""

from random import randint
"""Takes 2 integer arguments and returns randomly selected integer."""

print(randint(1,6))


from random import choice
"""Takes list or tuple and returns randomly chosen element."""

players = ['charles', 'eric', 'marina', 'edward', 'dave', 'michael', 'dean']

chosen = choice(players)

print(chosen.title())