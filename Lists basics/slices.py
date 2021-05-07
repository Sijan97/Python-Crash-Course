"""
Python Crash Course 
By Eric Matthes

Exercises: 4-10 to 4-12

"""

#Exercise 4-10

#Creating a list of birds and animals
pets = ['dog', 'cat', 'mouse', 'parrot', 'chicken', 'duck']
print(f"Animals in the list: {pets[:3]}")
print(f"Middle items in the list: {pets[2:4]}")
print(f"Birds in the list: {pets[3:]}")

#End of exercise 4-10

#Exercise 4-11

#Creating a list of pizzas
my_pizzas = ['chicken', 'cheese', 'pepperoni']
friend_pizzas = my_pizzas[:]
my_pizzas.append("mixed")
friend_pizzas.append("veg")
print(f"My favourite pizzas are:")
for pizza in my_pizzas:
	print(pizza.title())
print(f"My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(pizza.title())

#End of exercise 4-11

#Exercise 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are:")
for food in my_foods:
	print(food.title())
print("My friend's favourite foods are:")
for food in friend_foods:
	print(food.title())

#End of exercise 4-12