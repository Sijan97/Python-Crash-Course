"""Python Crash Course
By Eric Matthes

Dictionary tutorial
Definition: Dictionary is a collection of key-value pairs, where each key is 
connected to a value.

"""

#Syntax for creating a dictionary
alien_0 = {'color': 'green', 'points': 5}   #Dictionary is wrapped in braces.

#Accessing the values
print(f"Accessing value for key color: {alien_0['color'].title()}")
print(f"Accessing value for key points: {alien_0['points']}")

#Similar to lists, dictionaries are dynamic.

#Adding new key-value pair
alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(f"New dictionary: {alien_0}")

#Modifying dictionary
#Lets create a blank dictionary and add key-value pairs
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5

print(f"Dictionary: {alien_1}")

#Modifying color value
print(f"Initial alien color: {alien_1['color'].title()}")

alien_1['color'] = 'yellow'

print(f"Modified alien color: {alien_1['color'].title()}")

#Tracking the position and movement speed of alien
print(f"Initial x-position of alien: {alien_0['x-position']}")

#Adding alien movement speed
alien_0['speed'] = 'slow'

#Changing alien x-position minding speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x-position'] = alien_0['x-position'] + x_increment

print(f"New x-position of alien: {alien_0['x-position']}")

#Removing key-value pairs using del statement
print(f"Original dictionary: {alien_1}")

#Using key to remove key-value pair
del alien_1['points']

print(f"New dictionary: {alien_1}")

#Note: Deleted key-value pair is removed permanently.

#Storing same kind of information in dictionary.
favorite_languages = {
    'jen': 'java',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['jen']

if favorite_languages['jen'] == 'java':
    print(f"Jen's favorite programming language is: {language.upper()}")
else:
    print(f"Jen's favorite programming language is: {language.title()}")

#Using get to access value
print(alien_1)

#Trying to access value for point, which returns KeyError
#alien_1['point'] 

#In order to tackle KeyError get can be used
point_value = alien_1.get('point', 'Point key not available.')  

print(point_value)

#Note: get accepts 2 arguments, first for key and second for error message.

#Let's add key-value pair and again use get to access value
alien_1['point'] = 5

print(alien_1.get('point', 'No value for point.'))

#What if no message is given in second argument?
print(alien_1.get('x-position', ))

#Note: When there is no second argument passed, get returns None.