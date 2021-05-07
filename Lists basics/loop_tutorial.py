"""
Python Crash Course
By Eric Matthes

Loop tutorial 2

"""

#Creating list using range with 2 arguments
numbers = []
for value in range(1,10):
	numbers.append(value)
print(f"Items added using range:\n\t{numbers}")
#Note: When given parameters, the end value is not included.

#Creating list with 1 argument
numbers_1 = []
for value in range(10):
	numbers_1.append(value)
print(f"Items added using range:\n\t{numbers_1}")
#Note: When given only 1 argument, the list begins from 0.

#Creating list with 3 arguments
even_numbers = []
for value in range(2,11,2):
	even_numbers.append(value)
print(f"Items added using range:\n\t{even_numbers}")

"""
Note: The third argument specifies the items skipped in the range.
To understand simply, 2 is added every time the loop is passed.
In this case, loop begins from 2 and another 2 is added making another item 4
and so on.

"""

#Creating list of first 10 square numbers
square_numbers = []
for value in range(1,10):
	square_numbers.append(value**2)
print(f"Square numbers added:\n\t{square_numbers}")
#Note: ** is used to define exponents, hence value**2 tells the program to add square numbers from the range and add to the list.

#Simple Statistics and List Comprehensions
cubic_numbers = [cube**3 for cube in range(1,11)]	#Using list comprehension to reduce excessive lines of code
print(f"Cubic number added:\n\t{cubic_numbers}")

#Using simple stats to find minimum and maximum number in the list
print(f"Minumum number in the list: {min(cubic_numbers)}")
print(f"Maximum number in the list: {max(cubic_numbers)}")

#Sum of all numbers in the list
print(f"Sum of first 10 cube numbers: {sum(cubic_numbers)}")