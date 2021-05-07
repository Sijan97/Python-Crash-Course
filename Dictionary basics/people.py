"""Python Crash Course
By Eric Matthes

Exercises: 6-7 to 6-12
"""

#Exercise 6-7

#Making new dictionaries
friend1 = {
    'fname': 'rumi',
    'mname': 'bade',
    'lname': 'shrestha',
    'age': 23,
    'city': 'patan',
    }

friend2 = {
    'fname': 'pemba',
    'lname': 'lama',
    'age': 22,
    'city': 'kathmandu',
    }

friend3 = {
    'fname': 'sabin',
    'lname': 'kapali',
    'age': 24,
    'city': 'bhaktapur',
    }

friend4 = {
    'fname': 'santosh',
    'mname': 'lal',
    'lname': 'shrestha',
    'age': 43,
    'city': 'kathmandu',
    }

#Storing dictionary in a list
people = [friend1, friend2, friend3, friend4]

#Looping through the list
print("Friends around the valley:")

for friend in people:
    if 'mname' in friend:
        full_name = friend['fname'].title() + " " + friend['mname'].title()\
        + " " + friend['lname'].title()
        age = str(friend['age'])
        city = friend['city'].title()

        print(f"\t{full_name}, of {city}, is {age} years old.")
    else:
        full_name = friend['fname'].title() + " " + friend['lname'].title()
        age = str(friend['age'])
        city = friend['city'].title()

        print(f"\t{full_name}, of {city}, is {age} years old.")

    # print(f"\n\tFull name: {friend['fname'].title()} {friend['lname'].title()}")
    # print(f"\tAge: {friend['age']}")
    # print(f"\tCity: {friend['city'].title()}")

#End of exercise 6-7

#Exercise 6-8

#Making an empty list
pets = []

#Making animal dictionary
pet = {
    'type': 'dog',
    'name': 'pintu',
    'owner': 'sijan',
    'age': 5,
    'food': 'meat',
    }
pets.append(pet)

pet = {
    'type': 'cat',
    'name': 'snow',
    'owner': 'billy',
    'age': 2,
    'food': 'milk',
    }
pets.append(pet)

pet = {
    'type': 'mouse',
    'name': 'stuart',
    'owner': 'john',
    'age': 1,
    'food': 'nuts',
    }
pets.append(pet)

#Displaying information
for pet in pets:
    print(f"\nInformation about {pet['name'].title()}:")
    for info, details in pet.items():
        str_details = str(details)
        print(f"\t{info.title()}: {str_details.title()}")

#End of exercise 6-8

#Exercise 6-9
favorite_places = {
    'eric': ['mustang', 'rara', 'pokhara'],
    'sarah': ['swtizerland', 'amsterdam'],
    'dave': ['iceland'],
    }

for people, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{people.title()}'s favorite place is:")

        for place in places:
            print(f"-{place.title()}")
    else:
        print(f"\nHere's {people.title()}'s favorite places:")

        for place in places:
            print(f"-{place.title()}")

#End of exercise 6-9

#Exercise 6-10
favorite_numbers = {
    'eric': [1, 3 ,5 ,7],
    'dave': [2, 4, 6],
    'sarah': [3, 9],
    'matt': [10],
    'craig': [7, 13, 18, 17]
}

for person, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{person.title()}'s favorite number is:")

        for number in numbers:
            print("\t" + str(number))
    else:
        print(f"\n{person.title()}'s favorite numbers are:")

        for number in numbers:
            print("\t" + str(number))

#End of exercise 6-10

#Exercise 6-11
cities = {
    'kathmandu': {
        'country': 'nepal',
        'population': 256818,
        'fact': 'It is the capital of Nepal.',
        },
    'sikkim': {
        'country': 'india',
        'population': 12441,
        'fact': 'It has 11 official languages.',
        },
    'sydney': {
        'country': 'australia',
        'population': 20973,
        'fact': 'It is known for world reknown Sydney Opera House.',
        },
    }

for city, information in cities.items():
    print(f"\n{city.title()} is in {information['country'].title()}.")
    print(f"\tIt has a population of {information['population']} people.")
    print(f"\t{information['fact']}")

#End of exercise 6-11