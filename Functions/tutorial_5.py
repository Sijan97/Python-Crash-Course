"""Python Crash Course
By Eric Matthes

Tutorial: Arbitrary arguments"""

# Passing an arbitrary number of arguments
# Pizza toppings
def make_pizza(*toppings):
    """Printing the list of toppings that have been requested"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('cheese', 'mushroom', 'chicken')

# Note: * or (asterik) in the parameter lets the user to add as many
# arguments they want and adds the arguments to a tuple.

# Pizza toppings part two
def make_pizza2(*toppings):
    """Displaying the requested toppings in proper manner"""
    print("\nRequested toppings:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza2('cheese')
make_pizza2('pepperoni', 'mushroom', 'chicken')

# Mixing positional and arbitrary arguments
def make_pizza3(size, *toppings):
    """Displaying the size of pizza with requested toppings"""
    print(f"\nRequested toppings for {size}-inch pizza:")
    for topping in toppings:
        print(f"- {topping.title()}")

make_pizza3(12, 'chicken')
make_pizza3(16, 'mushroom', 'pepperoni', 'cheese')

# Using arbitrary keyword arguments
def build_profile(fname, lname, **user_info):
    """Build a dictionary about a person"""
    user_info['first_name'] = fname
    user_info['last_name'] = lname
    return user_info

user_profile = build_profile('sijan', 'shrestha', location='nepal', age=23)
print(f"\n{user_profile}")

# Note: ** before the parameter creates an empty dictionary parameter.