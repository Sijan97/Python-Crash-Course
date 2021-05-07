"""Python Crash Course
By Eric Matthes

Lopping tutorial

"""

user = {
    'username': 'sijan97',
    'first_name': 'sijan',
    'last_name': 'shrestha',
}

for key, value in user.items():
    if key == 'username':
        print(f"\nKey: {key}")
        print(f"\nValue: {value}")
    else:
        print(f"\nKey: {key}")
        print(f"\nValue: {value.title()}")
    #print(f"{key.title()}: {value.title()}")

"""Note: If-else statement is used because username should not be 
case-sensitive and first name and last name should be properly displayed.
"""

print(f"\nFull name: {user['first_name'].title()} {user['last_name'].title()}")

#Printing keys
for key in user.keys():
    print(f"\nKey: {key}")
#Note: for key in user.keys(): is same as for key in user:

#Printing greeting message to specific person with specific key
favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'python',
    'phil': 'ruby',
    'tony': 'java',
    'joe': 'angular',
    }

friends = ['jen', 'edward', 'tony']
for friend in favorite_languages:
    print("\nHi, "+ friend.title())

    if friend in friends:
        print(f"\t{friend.title()}, I see you love" \
            f" {favorite_languages[friend].title()}!")

#Printing message to person not included in dictionary
if 'sijan' not in favorite_languages:
    print("\nSijan, please take your poll!")

#Printing dictionary in particular order
for friend in sorted(favorite_languages):
    print(f"\nHi, {friend.title()}!")

#Printing out only values of dictionary
print("\nLanguages chosen for poll:")

for language in favorite_languages.values():
    print(language.title())

"""Note: The above program prints same value more than once,
which can be problematic for larger data."""

#Printing unique values using set() function
print("\nUnique languages:")

for language in set(favorite_languages.values()):
    print(language.title())

#Note:sorted function can be used to print values in particular order.