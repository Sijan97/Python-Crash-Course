"""
Python Crash Course
By Eric Matthes

Exercises: 9-13 to 9-16
"""

# Exercise 9-13
# Dice
from random import randint

class Die:
    """Prints a randomly chosen number."""
    def __init__(self, sides=6):
        """Initializing attribute."""
        self.sides = sides

    def roll_die(self):
        """Rolls the die and prints outcome."""
        return randint(1, self.sides)

# Making a 6-sided die and rolling 10 times
my_dice6 = Die()

result = []
for roll in range(10):
    roll = my_dice6.roll_die()
    result.append(roll)

print("10 rolls of a 6-sided die:")
print(result)

# Making a 10-sided die and rolling 10 times
my_dice10 = Die(10)

result10 = []
for roll in range(10):
    roll = my_dice10.roll_die()
    result10.append(roll)

print("\n10 rolls of a 10-sided die:")
print(result10)

# Making a 20-sided die and rolling 10 times
my_dice20 = Die(20)

result20 = []
for roll in range(10):
    roll = my_dice20.roll_die()
    result20.append(roll)

print("\n10 rolls of a 20-sided die:")
print(result20)

# End of exercise 9-13

# Exercise 9-14
# Lottery
from random import choice

lucky = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

lottery = []
for winner in range(4):
    winner = choice(lucky)
    lottery.append(winner)

print("\nWinning number or letter:")
print(lottery)

# End of exercise 9-14