"""
Python Crash Course
By Eric Matthes

Exercises: 4-3 to 4-9

"""

#Exercise 4-3

#Making a list of number from 1 to 20 inclusive
num_20 = []
for number in range(1,21):
	num_20.append(number)
print(f"Numbers added to twenty: \n\t{num_20}")

#Using list comprehension to solve above problem
num_201 = [number for number in range(1,21)]
print(f"Numbers added using list comprehension: \n\t{num_201}")

#End of exercise 4-3

#Exercise 4-4

#Printing one million numbers
millions = [million for million in range(1,100000)]
print(f"Millions of numbers:\n\t{millions}")

#End of exercise 4-4

#Exercise 4-5

#Applying basic stats in millions
print(f"Minimum number in the list of millions: {min(millions)}")
print(f"Maximum number in the list of millions: {max(millions)}")
print(f"Sum of millions: {sum(millions)}")

#End of exercise 4-5

#Exercise 4-6

#List of odd numbers
odds = [odd for odd in range(1,20,2)]
print(f"List of odd numbers: \n\t{odds}")

#End of exercise 4-6

#Exercise 4-7

#List of multiples of 3
threes = [three for three in range(3,30,3)]
print(f"Multiples of three: \n\t{threes}")

#End of exercise 4-7

#Exercise 4-8

#List of cubes without list comprehension
cubes_1 = []
for cube in range(1,11):
	# cube = cube**3
	# cubes_1.append(cube)
	#Or omit execcive lines of code:
	cubes_1.append(cube**3)
print(f"List of cubes without list comprehension: \n\t{cubes_1}")

#End of exercise 4-8

#Exercise 4-9

#List of cubes using list comprehension
cubes = [cube**3 for cube in range(1,11)]
print(f"List of cubes using list comprehension: \n\t{cubes}")

#End of exercise 4-9