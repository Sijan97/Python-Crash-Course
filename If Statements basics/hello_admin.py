"""Python Crash Course
By Erict Matthes

Exercises: 5-8 to 5-11

"""

#Exercise 5-8
users = ['admin', 'adam', 'steve', 'james', 'dave']

for user in users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")

#End of exercise 5-8

#Exercise 5-9
usernames = []

if usernames:
    for username in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

#End of exercise 5-9

#Exercise 5-10
current_users = ['eRic', 'adAM', 'steve', 'james', 'dave']
new_users = ['toby', 'MicHael', 'eRiC', 'ADAM', 'sam']

current_users = [current_user.lower() for current_user in current_users]
print(f"New copy of lowered users: {current_users}")
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username {new_user.title()} is taken!")
    else:
        print(f"Username {new_user.title()} available!")

#End of exercise 5-10

#Exercise 5-11
#numbers = [number for number in range(1,10)]
numbers = list(range(1,10))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
        
#End of exercise 5-11