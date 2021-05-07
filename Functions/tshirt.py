"""Python Crash Course
By Eric Matthes

Exercises: 8-3 to 8-5"""

# Exercise 8-3
# T-Shirt
def make_shirt(size, message):
    """Display shirt details."""
    print(f"Size: {size}")
    print(f"Message: {message}.\n")

# Calling the function using positional arguments.
make_shirt('XXL', 'Legend sice 1997')

# Calling the function using keyword arguments.
make_shirt(size='XXL', message='Save earth')

# End of exercise 8-3

# Exercise 8-4
# Large Shirts
def make_shirt(size='large', message='I love Python'):
    """Summarize the shirt that is going to be made."""
    print(f"I made {size} shirt with message: {message}.")

# Calling the function
make_shirt()
make_shirt('medium')
make_shirt('extra large', 'Legend since 1997')
make_shirt(message='Save earth', size='small')

# End of exercise 8-4

# Exercise 8-5
# Cities
def describe_city(name, country='nepal'):
    """Describing a city."""
    print(f"\n{name.title()} is in {country.title()}.")

# Calling the function
describe_city('kathmandu')
describe_city(name='pokhara')
describe_city(country='India', name='sikkim')
describe_city('darjeeling', 'nepal')

# End of exercise 8-5