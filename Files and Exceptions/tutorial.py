"""
Python Crash Course
By Eric Matthes

Tutorial: Reading Files
"""

# Reading a file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()

print(contents)

# Reading a file giving relative path
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()

print(f"\n{contents}")

# Reading a file giving absolute path
filepath = 'd:/Docs/python_work/Files and Exceptions/text_files/pi_digits.txt'

with open(filepath) as file_object:
    contents = file_object.read()

print(f"\n{contents}\n")

# Reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

# Modifying a line
print("")

with open(filename) as file_object:
    for line in file_object:
        if 'Python files' in line:
            line = 'Digits in a pi'
            print(line.rstrip())
        else:
            print(line.rstrip())

# Making a list of lines from a file
print("")

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Note: Each line in the lines list is considered seperate index item.

# Working with a file's contents
print("")

with open(filename) as file_object:
    lines = file_object.readlines()

# Variable to hold the contents of the list
pi_string = ''
for line in lines:
    if 'Python files' in line:
        line = ''
    else:
        pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Large files: One million digits
print("")

filepath = 'D:/Docs/PCC Downloads/ehmatthes-pcc-f555082/chapter_10'
filepath += '/pi_million_digits.txt'

with open(filepath) as file_object:
    contents = file_object.readlines()

pi_million_strings = ''

for content in contents:
    pi_million_strings += content.strip()

print(pi_million_strings[:50])
print(len(pi_million_strings))

# Checking if birthday appear in pi
birthday = input('Enter your birthdate, in the form mmddyy: ')

if birthday in pi_million_strings:
    print("Your birthday appears in first million digits of pi!")
else:
    print("Your birthday does not appear in first million digits of pi.")