"""
Python Crash Course 
By Eric Matthes

Exercises: 10-1 to 10-2
"""

# Exercise 10-1
# Learning Python
class FileReader:
    """Reads a text file and prints the contents of the file."""
    def __init__(self, filepath):
        """Initializing attribute."""
        self.filepath = filepath

    def read_file(self):
        """Opens and reads the file."""
        with open(self.filepath) as file_object:
            contents = file_object.read()

            print(contents.rstrip())

    def loop_file(self):
        """Opens file and loops inside the line."""
        print('')

        with open(self.filepath) as file_object:
            for content in file_object:
                print(content.rstrip())

    def open_file(self):
        """Opens file and stores file object to use outside with block."""
        print('')

        with open(self.filepath) as file_object:
            contents = file_object.readlines()

        # for content in contents:
        #     print(content.rstrip())
        return contents

# Making object
my_file = FileReader('text_files/learning_python.txt')

my_file.read_file()
my_file.loop_file()

for content in my_file.open_file():
    print(content.rstrip())

# End of exercise 10-1

# Exercise 10-2
# Learning C
for content in my_file.open_file():
    # new_content = content.replace('Python', 'C')
    # print(new_content.rstrip())

    print(content.replace('Python', 'C').rstrip())

# End of exercise 10-2