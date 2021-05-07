"""
Python Crash Course
By Eric Matthes

Slicing tutorial:
Slice is a part of the list seperated from specific index.

"""

#Creating list of fruits and vegetables

items = ['orange', 'mango', 'banana', 'apple', 'carrot', 'radish', 'eggplant', 'spinach']
print(f"Seperated list of fruits: \n\t{items[0:4]}")	#Slicing requires index to be passed
print(f"Seperated list of vegetables: \n\t{items[4:]}")	#When not given any end or starting index, slicing always determines 0 index or last index

#Looping through the slice
print("Here is the list of fruits:")
for item in items[:4]:
	print(item.title())

#Copying a slice
foods = ['momo', 'pizza', 'burger', 'tandoori', 'chowmein', 'naan', 'fries']
my_foods = foods[:4]
print(f"These are my favourite foods: \n\t{my_foods}")
friends_foods = my_foods[:]
print(f"These are my friend's favourite foods: \n\t{friends_foods}")

#Note: The slice copied to another variable is not related to first slice/list. So any changes in any list won't affect another.