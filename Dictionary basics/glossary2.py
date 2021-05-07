"""Python Crash Course 
By Eric Matthes

Exercises: 6-4 to 6-6
"""

#Exercise 6-4

glossary = {
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    'tuple': 'A static list.',
    'float': 'Decimal value.',
    'parentheses': 'Brackets'
    }

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")

#End of exercise 6-4

#Exercise 6-5

rivers = {
    'nile': 'egypt',
    'ganga': 'india',
    'bagmati': 'nepal',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.\n")

print("Rivers in dictionary:")

for river in rivers:
    print(river.title())

print("\nCountries in dictionary:")

for country in rivers.values():
    print(country.title())

#End of exercise 6-5

#Exercise 6-6

favorite_languages = {
    'python': 'sijan',
    'java': 'sam',
    'c': 'matt',
    'ruby': 'dean',
    'angular': 'paul',
    }

friends = ['dean', 'paul', 'harry', 'tom', 'ron', 'sijan']

for friend in friends:
    if friend.lower() in favorite_languages.values():
        print(f"\nHi {friend.title()}, thank you for taking the poll!")
    else:
        print(f"\nHi {friend.title()}, please take your poll!")

#End of exercise 6-6