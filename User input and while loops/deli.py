""" Python Crash Course
By Eric Matthes

Exercises: 7-8 to 7-10
"""

# Exercise 7-8
# Deli
sandwich_orders = ['tuna', 'egg', 'chicken', 'buff']
finished_sandwiches = []

print("Processing orders:")

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"\tI made your {order} sandwich.")

    finished_sandwiches.append(order)

print("\nCompleted orders:")

for completed in finished_sandwiches:
    print(f"\t{completed.title()} sandwich")

# End of exercise 7-8

# Exercise 7-9
# No pastrami
sandwich_orders = [
    'pastrami', 'tuna', 'pastrami',
    'egg', 'chicken',
    'pastrami', 'buff'
    ] 
finished_sandwiches = []

print("\n------ Note: We are out of pastrami today! ------")
print("\nProcessing orders:")

while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

    ordered = sandwich_orders.pop()
    print(f"\tI have made your {ordered} sandwich.")

    finished_sandwiches.append(ordered)

print("\nCompleted Orders:")

for completed in finished_sandwiches:
    print(f"\t{completed.title()} sandwich")

# End of exercise 7-9

# Exercise 7-10
# Dream vacation
result = {}

while True:
    names = input("\nPlease state your name: ")
    places = input("Place you would like to visit one day: ")

    result[names] = places
    repeat = input("\nAny one wants to join the poll?(Enter yes/no) ")

    if repeat.lower() == 'no':
        break
    
print("\nPoll result:")
for name, place in result.items():
    print(f"\t{name.title()} would like to visit {place.title()} one day.")
