#Sorting elements of the list in alphabetical order
bikes = ["yamaha", "suzuki", "bmw", "honda"]
print(bikes)
bikes.sort()
print(bikes)

#In order to arrange in reverse alphabetical order, reverse=true argument is passed
bikes.sort(reverse=True)
print(bikes)

# Key note: sort() is used to permanently sort the items of the list

# Temporary sorting of the list using sorted()

print(f"Original list:\n\t{bikes}")
print(f"Temporarily sorted list:\n\t{sorted(bikes)}")
print(f"Original list again:\n\t{bikes}")

#Printing a list in reverse order
print(bikes)
bikes.reverse()	#Reverse is permanent.
print(bikes)

#Finding the length of the list
print(f"{len(bikes)}")