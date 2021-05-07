"""
Python Crash Course 
By Eric Matthes

Tutorial: unittesting module
"""

# Testing a function
# name_function.py
def get_formatted_name(first, last, middle=''):
    """Returns neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

# print("Enter 'q' at anytime to quit.")

# while True:
#     first = input("First name: ")
#     if first == 'q':
#         break
#     last = input("Last name: ")
#     if last == 'q':
#         break

#     full_name = get_formatted_name(first, last)
#     print(f"\nNeatly formatted name: {full_name}.")    

# test_name_function.py
import unittest

class NamesTestCase(unittest.TestCase):
    """Tests for name_function.py"""
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()