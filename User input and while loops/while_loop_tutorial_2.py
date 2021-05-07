"""Python Crash Course
By Eric Matthes

Tutorial: While loop with lists and dictionaries
"""

# Confirmed Users

# Create a list of users that need to be verified,
# and another list to hold the confirmed users.
users = ['alice', 'brian', 'candace']
verified_users = []

# Verify all users until there are no more unconfirmed users.
# Move each verified user to verified_users list.

print("Users that need to be verified:")
for user in users:
    print(f"\t{user.title()}")

print("\nVerification on process:")

while users:
    verify = users.pop()

    print(f"\t{verify.title()} is being verified.")
    verified_users.append(verify)

    print(f"\t{verify.title()} is verified.")

print(f"\nVerified users:")

for user in verified_users:
    print(f"\t{user.title()}")

# Removing all instances of specific values from a list.

# Removing value from a normal list.
animals = ['dog', 'cat', 'rabbit', 'fish', 'cat', 'dog', 'fish']

print(f"\nTotal number of animals: {len(animals)}")
animals.remove('cat')

print(f"\nTotal number animals after removing: {len(animals)}")
print(f"After removing: {animals}")

# Note: In above example, only one instance of item is removed.
# That is where while loop comes handy.

animals.append('cat')
print(f"\nList of animals: {animals}")

# Lets remove 'cat' again, but using while.
while 'cat' in animals:
    animals.remove('cat')

print(f"\nNew list after remove: {animals}")

# Filling a dictionary with user input.

#Favorite country.
responses = {}

polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input(f"\nWhat is your name? ")
    response = input("Which country would you like to visit? ")

    # Storing the name and response in dictionary.
    responses[name] = response

    # Repeat or quit the poll.
    repeat = input("Anyone wants to join the poll?(yes/no) ")

    if repeat == 'no':
        polling_active = False

# Polling Complete.
print(f"\nPoll result:")

for name, response in responses.items():
    print(f"{name.title()} loves to vist {response.title()} one day.")