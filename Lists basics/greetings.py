"""
Python Crash Course
By Eric Matthes

Exercises: 3-1 to 3-3

"""

#Exercise 3-1
names = ["sanam", "sajik", "nishan", "ROHIT"]

#Exercise 3-2
greets = ["hello, ", "good morning, ", "hi, "]
print(f"{greets[0].rstrip().title()}{names[0].title()}")		#Practice of rstrip
print(f"{greets[1].title()}{names[1].title()}\n{greets[2].title()}{names[2].upper()}\n{greets[0].title()}{names[-1].lower()}")		#Use of name cases