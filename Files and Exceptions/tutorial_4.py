"""
Python Crash Course
By Eric Matthes

Tutorial: Storing data/JSON
"""

# Using json.dump() and json.load()
import json

numbers = [1, 2, 3, 4, 5, 6]
filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

# Reading the json file
with open(filename) as f:
    json_numbers = json.load(f)

print(json_numbers)