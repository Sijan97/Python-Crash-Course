"""
Python Crash Course
By Eric Matthes

Tutorial: Writing to a file
"""
filepath = 'text_files/programming.txt'

with open(filepath, 'w') as file_object:
    file_object.write("I love programming.")

with open(filepath.replace('programming.txt', 'numbers.txt'), 'w') as f:
    f.write(str(123456))

# Note: In order to save numerical data convert to string first.

# Writing multiple lines
with open(filepath, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating games.\n")

# Appending to a file
with open(filepath, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love solving complex problems.\n")

# Reading the final version of the file we created
with open(filepath) as file_object:
    print(file_object.read().rstrip())