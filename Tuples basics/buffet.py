"""
Python Crash Course
By Eric Matthes

Exercise 4-13

"""

#Defining tuple
foods = ('momo', 'chowmein', 'thukpa', 'noodles', 'fried rice')
print("We serve:")
for food in foods:
    print(f"\t{food.title()}")

#Trying to modify the tuple
#foods[1] = "Egg rice"
#TypeError generated

#Redefining tuple
foods = ('laphing' , 'spaghetti' , 'chowmein', 'noodles', 'thukpa')
print("Revised menu:")
for food in foods:
    print(f"\t{food.title()}")

#End of exercise 4-13