"""Python Crash Course
By Eric Matthes

Tutorial: While loop
"""

#Counting
number = 0

while number <= 5:
    print(f"\n The number is now {number}.")

    number += 1

#Parrot
prompt = "\nType something and i will repeat:"
prompt += "\nType 'quit' to exit program. "
message = ""

while message.lower() != 'quit':
    message = input(prompt)
    
    if message.lower() != 'quit':
        print(message)

#Parrot with flag
parrot = "\nType something and i will repeat:"
parrot += "\nType 'quit' or 'exit' to exit program. "
status = True

while status:
    message = input(parrot)
    
    if message.lower() == 'quit':
        status = False
    elif message.lower() == 'exit':
        status = False
    else:
        print(message)

#Using break to exit the loop
user_input = "\nCity you have visited:"
user_input += "\n(Type 'quit' or 'exit' to exit the program.) "

while True:
    city = input(user_input)

    if city.lower() == 'quit' or city.lower() == 'exit':
        break
    else:
        print(f"I would love to visit {city.title()}!")

#Using continue in a loop

#Counting odd
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
        
    print(f"The current number is {current_number}")