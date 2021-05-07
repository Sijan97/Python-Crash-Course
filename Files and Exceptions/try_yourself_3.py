"""
Python Crash Course
By Eric Matthes

Exercises: 10-6 to 10-10
"""

# Exercise 10-6
# Addition
try:
    first_number = input('First number: ')
    second_number = input('Second number: ')
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Please provide numbers.")
else:
    print(f"Answer: {answer}")

# End of exercise 10-6

# Exercise 10-7
# Addition Calculator
print("\nProvide two numbers for addition.")
print("Enter 'q' anytime to quit.")

while True:
    try:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break

        second_number = input("Second number: ")
        if second_number == 'q':
            break

        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter a number.")
    else:
        print(f"Answer: {answer}")

# End of exercise 10-7

# Exercise 10-8
# Cats and Dogs
print('')

# with open('cats.txt', 'w') as f:
#     f.write('Snow\n')
#     f.write('Bell\n')
#     f.write('Chunky\n')

# with open('dogs.txt', 'w') as f:
#     f.write('Pintu\n')
#     f.write('Tony\n')
#     f.write('Tommy\n')


def file_reader(filenames):
    """Reads the contents of a file."""
    try:
        with open(filenames) as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Sorry, the file '{filenames}' does not exist.")

filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    file_reader(file)

# End of exercise 10-8

# Exercise 10-9
# Silent Cats and Dogs
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)

# End of exercise 10-9

# Exercise 10-10
# Analyzing text
# Counting number of 'the' in Alice in Wonderland
with open('alice.txt', encoding='utf-8') as f:
    contents = f.read()
    count_the = contents.lower().count('the ')

    print(f"Number of 'the': {count_the}")

# End of exercise 10-10