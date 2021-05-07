"""Python Crash Course
By Eric Matthes

If Statements tutorial

"""

#Defining a list of cars
cars = ['audi', 'bmw', 'subaru', 'toyota']
print("Car models:")

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Conditional true and false
car = 'BMW'
print(car == 'bmw')
#This statement returns false because python is case sensitive.

print(car == 'BMW')
#Now this statement returns true

#Ignoring name case
print(car.lower() == 'bmw') #This is a true statement.

#Inequalities
topping = 'mushrooms'

if topping != 'anchovies':
    print("Hold the anchovies!")

#Number comparisons
number = 21

if number != 97:
    print("Not the right number!")

age_0 = 21
age_1 = 45

if age_0 >= 18 and age_1 <= 50:
    print("Eligible age!")

if age_0 != 18 and age_0 < 18:
    print("Not Eligible!")

if age_0 > 18 or age_1 != 50:
    print("Eligible age!")

#Checking if a value exists in a list
toppings = ['chicken','mushrooms', 'pepperoni']

if 'chicken' in toppings:
    print("Chicken topping added!")

if 'pineapple' not in toppings:
    print("Pineapple topping not added!")

#Banned users
banned_users = ['andrew', 'carolina', 'sam']
user = 'drake'

if user not in banned_users:
    print(f"{user.title()} is allowed in the server!")

user = 'andrew'

if user in banned_users:
    print(f"{user.title()} has been banned from the server!")