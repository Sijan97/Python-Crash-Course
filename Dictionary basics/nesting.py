"""Python Crash Course
By Eric Matthes

Nesting tutorial
"""

#Making a list of different aliens

#Creating 3 different dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#Storing above dictionaries in a new list
aliens = [alien_0, alien_1, alien_2]

#Printing the list
for alien in aliens:
    print(alien)

#Using range() to create a list of 30 aliens

#Make an empty list to store aliens
aliens1 = []

#Make 30 green aliens
for add_aliens in range(30):
    new_alien = {'color': 'green', 'speed': 'slow', 'points': 5}
    aliens1.append(new_alien)

#First 5 aliens
for aliens in aliens1[0:5]:
    print(f"\n{aliens}")

#Total number of aliens created
print(f"\nTotal number of aliens: {len(aliens1)}.")

#Modifying first 3 aliens
for alien in aliens1[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens1[:10]:
    print(f"\n{alien}")

#List in a dictionary 

#Pizza toppings
pizza = {
    'crust': 'thick',
    'toppings': ['pepperoni', 'mushrooms', 'extra cheese'],
    }

print(f"\nYou ordered a {pizza['crust']}-crust pizza with following toppings:")

for topping in pizza['toppings']:
    # print(f"{topping.title()}")
    print("\t" + topping.title())

#Favorite languages
friends = {
    'jen': ['java', 'angular'],
    'sarah': ['c'],
    'paul': ['python', 'ruby'],
    'sijan': ['python', 'c#'],
    'tom': ['java'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for friend, languages in friends.items():
    if len(languages) > 1:
        print(f"\n{friend.title()}'s favorite languages are:")

        for language in languages:
            print(f"\t{language.title()}")

        if 'python' in languages:
            print(f"\tHi {friend.title()}, I see you love python!")
    
    if len(languages) == 1:
        print(f"\n{friend.title()}'s favorite language is")

        for language in languages:
            print("\t" + language.title())

#Dictionary in a dictionary
users = {
    'aeinstein': {
        'fname': 'albert',
        'lname': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'fname': 'marie',
        'lname': 'curie',
        'location': 'paris',
        },
    }

print("\nUser details:")

for username, details in users.items():
    print(f"\tUsername: {username}")
    print(f"\tFull name: {details['fname'].title()} {details['lname'].title()}")
    print(f"\tLocation: {details['location'].title()}\n")