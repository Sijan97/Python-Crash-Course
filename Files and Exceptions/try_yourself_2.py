"""
Python Crash Course
By Eric Matthes

Exercises: 10-3 to 10-5
"""

# Exercise 10-3
# Guest
def guest_list():
    """Takes name as input and saves the input in a file named guest.txt"""
    filepath = 'text_files/guest.txt'
    name = input("State your name: ")

    with open(filepath, 'w') as file_object:
        file_object.write(name)

guest_list()

# End of exercise 10-3

# Exercise 10-4
# Guest Book
filepath = 'text_files/guest_book.txt'

print("\nEnter 'quit' anytime to exit.")

while True:
    name = input("State your name: ")

    if name == 'quit':
        break
    else:
        with open(filepath, 'a') as file_object:
            file_object.write(f"{name.title()}\n")

        print(f"Hello {name.title()}, you have been added to the guest list.")

# End of exercise 10-4

# Exercise 10-5
# Programming poll
filepath = 'text_files/programming_poll.txt'

responses = []

while True:
    response = input("\nWhy do you like programming?\n")
    responses.append(response)

    continue_poll = input("\nAnyone wants to poll? (y/n): ")
    if continue_poll == 'n':
        break

with open(filepath, 'a') as file_object:
    for response in responses:
        file_object.write(f"{response}\n")

# End of exercise 10-5