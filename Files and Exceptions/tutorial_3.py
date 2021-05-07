"""
Python Crash Course
By Eric Matthes

Tutorial: Exception Handling
"""

# ZeroDivisionError
# print(5/0) raises error so we use try-except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero!")

# More practical example
print("Give me two numbers for division.")
print("Enter 'quit' anytime to exit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'quit':
        break

    second_number = input("Second number: ")
    if second_number == 'quit':
        break

    try:
        division = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    else:
        print(f"Answer: {division}")

# FileNotFoundError
# Trying to read alice.txt
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}' does not exist.")

# Analyzing text
# Counting number of words in Alice in Wonderland book
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file '{filename}'' does not exist.")
else:
    words = contents.split()
    num_of_words = len(words)

    print(f"The file '{filename}' has about {num_of_words} words.")


# Working with multiple files
def count_words(filename):
    """Counts the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file '{filename}'' does not exist.")
        pass    # This shows nothing to the user.
    else:
        words = contents.split()
        num_of_words = len(words)

        print(f"The file '{filename}' has about {num_of_words} words.")

filenames = [
    'alice.txt', 
    'siddhartha.txt', 
    'moby_dick.txt', 
    'little_women.txt'
    ]

for file in filenames:
    count_words(file)