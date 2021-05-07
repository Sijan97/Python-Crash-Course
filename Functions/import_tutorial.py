"""Python Crash Course
By Eric Matthes

Tutorial: Importing module"""

import tutorial_6

tutorial_6.make_pizza(12, 'pepperoni')
tutorial_6.make_pizza(16, 'extra cheese', 'mushroom', 'chicken')

# Other import statements:
"""Importing specific function:
-from tutorial_6 import make_pizza()

Using alias for function:
from tutorial_6 import make_pizza as mp

Using alias for module:
import tutorial_6 as t

Importing all functions in a module:
from tutorial_6 import *"""