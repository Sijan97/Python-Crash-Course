"""Python Crash Course
By Eric Matthes

Exercises: 6-1 to 6-3

"""

#Exercise 6-1

person = {
    'first_name': 'rumi',
    'last_name': 'shrestha',
    'age': 23,
    'city': 'patan',
    }

print(f"First name: {person['first_name'].title()}")
print(f"Last name: {person['last_name'].title()}")
print(f"Age: {person['age']}")
print(f"City: {person['city'].title()}")

#End of exercise 6-1

#Exercise 6-2

favorite_numbers = {
    'sijan': 20,
    'rumi': 18,
    'sajik': 10,
    'rohit': 8,
    'nishan': 9,
    }

num = favorite_numbers.get('sijan',)
print(f"Sijan's favorite number is: {num}")

num = favorite_numbers.get('rumi',)
print(f"Rumi's favorite number is: {num}")

num = favorite_numbers.get('sajik')
print(f"Sajik's favorite number is: {num}")

num = favorite_numbers.get('rohit')
print(f"Rohit's favorite number is: {num}")

num = favorite_numbers.get('nishan')
print(f"Nishan's favorite number is: {num}")

#End of exercise 6-2

#Exercise 6-3
glossary ={
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': 'A collection of key-value pairs.',
    }

print(f"\nString: {glossary.get('string',)}")
print(f"\nComment: {glossary.get('comment',)}")
print(f"\nList: {glossary.get('list',)}")
print(f"\nLoop: {glossary.get('loop',)}")
print(f"\nDictionary: {glossary.get('dictionary',)}")

#End of exercise 6-3