"""Python Crash Course
By Eric Matthes

Exercises: 7-4 to 7-7
"""

#Exercise 7-4
u_input = "Please select your toppings:"
u_input += "\n(Please type 'quit' or 'exit' to quit.) "

while True:
    topping = input(u_input)

    if topping.lower() == 'exit' or topping.lower() == 'quit':
        break
    else:
        print(f"{topping.title()} is added to the topping!\n")

#End of exercise 7-4

#Exercise 7-5
prompt = "Please enter your age:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    age = input(prompt)

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Free ticket!")
    elif age >= 3 and age < 12:
        print("Ticket price: $10")
    else:
        print("Ticket price: $15")

#End of exercise 7-5