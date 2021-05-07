"""Python Crash Course
By Eric Matthes

Exercises: 7-1 to 7-3
"""

#Exercise 7-1
car = input("What kind of car would you like to rent? ")

print(f"Let me see if I can find you a {car}.")

#End of exercise 7-1

#Exercise 7-2
people = input("\nNumber of people attending dinner: ")
people = int(people)

if people > 8:
    print("Please wait while we find you an open table.")
else:
    print(f"Table for {people} is ready!")

#End of exercise 7-2

#Exercise 7-3
number = input("\nEnter a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")

#End of exercise 7-3
