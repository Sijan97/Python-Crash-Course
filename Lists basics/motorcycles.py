# Modifying the elements of the list
brands = ["yamaha", "suzuki", "honda"]
print(brands)
brands[0] = "ducati"
print(brands)

# Adding elements to the list
brands.append("yamaha")	# Append adds new element to the end of the list
print(brands)

# Adding elements to empty list
cars = []
cars.append("bmw")
cars.append("volkswagen")
cars.append("skoda")
print(cars)

# Inserting new element to the list
cars.insert(0, "Land Cruiser")	#Insert lets you choose the index where element is added
print(cars)

# Removing an element from the list
del brands[0]	# del is a statement used to remove an element from the list
print(brands)

# Removing an item using pop
popped_cars = cars.pop()	# pop removes the last item to the list
print(cars)
print(popped_cars)

# Using pop to remove item in specific index
print(brands)
brands.append("ducati")
first_bike = brands.pop(0)
print(brands)
print(f"My first bike was {first_bike}.")

# Removing an item by value
cars.append("toothpaste")
print(cars)
removed_item = "toothpaste"
cars.remove(removed_item)
print(cars)
print(f"I removed {removed_item}, because it is not a car.")