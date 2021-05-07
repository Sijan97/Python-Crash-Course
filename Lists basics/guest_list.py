"""
Python Crash Course
By Eric Matthes

Exercises: 3-4 to 3-7 and 3-9

"""

#Creating an empty list to add new guests
#Exercise 3-4
guests = []
guests.append("sanjay")
guests.append("shreyash")
guests.append("mukesh")
greets = ["welcome", "greetings", "hello"]
print(f"{greets[0].title()}, {guests[0].title()} thank you for visiting!!!\
	\n{greets[1].title()}, {guests[1].title()} thank you for visiting!!!\
	\n{greets[2].title()}, {guests[2].title()} thank you for visiting!!!")

#Removing a guest and displaying the name
#Exercise 3-5
failed_guest = "mukesh"
guests.remove(failed_guest)
print(f"Unfortunately, {failed_guest.title()} would not be able to attend today.")

# Adding new guest for replacement
#guests.insert(2, "Pemba")
guests.append("pemba")
print(guests)

#Invitation messages
print(f"{greets[0].title()}, {guests[0].title()} thank you for visiting!!!\
	\n{greets[1].title()}, {guests[1].title()} thank you for visiting!!!\
	\n{greets[2].title()}, {guests[2].title()} thank you for visiting!!!")

#Adding new guests
#Exercise 3-6
guests.insert(0, "sajik")
guests.insert(2, "rohit")
guests.append("nishan")

#Removing guests
#Exercise 3-7
popped_guest1 = guests.pop()
print(f"I deeply regret to infrom {popped_guest1.title()} that your invitation has been cancelled")
popped_guest2 = guests.pop()
print(f"I deeply regret to infrom {popped_guest2.title()} that your invitation has been cancelled")
popped_guest3 = guests.pop(1)
print(f"I deeply regret to infrom {popped_guest3.title()} that your invitation has been cancelled")
popped_guest4 = guests.pop(0)
print(f"I deeply regret to infrom {popped_guest4.title()} that your invitation has been cancelled")
print(guests)

#Clearing the list using del
del guests[0]
del guests[0]
print(guests)

#Exercise 3-9
print(f"Today I am going to have {len(guests)} guests for dinner.")