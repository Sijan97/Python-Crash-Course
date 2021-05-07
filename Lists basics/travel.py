"""
Python Crash Course
By Eric Matthes

Exercises: 3-8 to 3-10

"""

#Exercise 3-8
#Temporary Sorting in alphabetical and reverse alphabetical order

places = ['taplejung', 'rara', 'mustang', 'annapurna', 'namche']
print(f"Travel destinations in original list:\n\t{places}")
print(f"Travel destinations temporarily sorted:\n\t{sorted(places)}")
print(f"Unaffected original list:\n\t{places}")
print(f"Temporary sorting in reverse alphabetical order:\n\t{sorted(places,reverse=True)}")
print(f"Unaffected original list:\n\t{places}")

#Using reverse to change the order of the list

places.reverse()
print(f"List in reverse order:\n\t{places}")
places.reverse()
print(f"List reversed again to attain original order:\n\t{places}")

#Permanent Sorting in alphabetical and reverse alphabetical order
places.sort()
print(f"Permanently sorted list in alphabetical order:\n\t{places}")
places.sort(reverse=True)
print(f"List sorted in reverse alphabetical order:\n\t{places}")

#End of exercise 3-8

#Exercise 3-10 (Chapter summarization)
#Creating an empty list and adding items using append
pets = []
pets.append('dog')
pets.append('cat')
pets.append('mouse')
pets.append('bird')
pets.append('rabbit')
print(pets)

#Accessing specific element and printing a message
print(f"I love having a pet {pets[0].title()}.")
print(f"List start from index 0: {pets[0].title()}")
print(f"Last item of the list can be accessed using -1 index: {pets[-1].title()}")

#Changing, adding and removing elements in the list
pets[-1] = "horse"
print(f"Above line replaces the last element item with new item assigned, hence new list becomes:\n\t{pets}")
#Adding new elemets using append and insert
pets.append("rabbit")
print(f"Append adds new item to the list at the end:\n\t{pets}")
pets.insert(3, "cow")
print(f"Insert can be used to add elements in any index:\n\t{pets}")

#Removing elements from the list
print(f"Here is the list:\n\t{pets}")
del pets[-1]
print(f"Del removes the element specified permanently, so new list becomes:\n\t{pets}")
popped_item = pets.pop()
print(f"Pop removes last element from the list but lets you to use the value, here we can see the item removed: {popped_item.title()}")
popped_item1= pets.pop(3)
print(f"Pop can also be used to remove value from any index, from above line, {popped_item1.title()} is removed.")
print(f"Remaining list items:\n\t{pets}")
removed_pet = "bird"
pets.remove(removed_pet)
print(f"Here we can see that 'bird' is removed from the list and the remaining list is:\n\t{pets}")
print(f"Similar to pop, remove can also be used to store the value removed, in this case: {removed_pet.title()}")

#Sorting the list 
print(f"Remaining items in the list:\n\t{pets}")
pets.append("rabbit")
pets.append("bird")
pets.append("horse")
print(f"New list:\n\t{pets}")
pets.sort()
print(f"New alphabetically sorted list:\n\t{pets}")
pets.sort(reverse=True)
print(f"List sorted reverse reverse alphabetically:\n\t{pets}")
print(f"Temporary sorting of list:\n\t{sorted(pets)}")
print(f"Unaltered list order:\n\t{pets}")
pets.sort()
print(f"List sorted alphabetically:\n\t{pets}")
print(f"Temporary sorting of list in reverse alphabetical order:\n\t{sorted(pets,reverse=True)}")
print(f"Unaltered list order:\n\t{pets}")

#Arranging the list in reverse order
print(f"List order:\n\t{pets}")
pets.reverse()
print(f"List in reverse order:\n\t{pets}")

#Finding the length of the list
print(f"Total items in the list: {len(pets)}")

#End of the exercise 3-10