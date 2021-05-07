"""Python Crash Course
By Eric Matthes

Tutorial: Modules"""

# Storing your functions in modules
# Importing an entire module
# A module is a file ending in .py
# Making a module that contains the program to make a pizza
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nRequested toppings for {size}-inch pizza:")

    for topping in toppings:
        print(f"- {topping.title()}")

# Save this module and create another module to import this module.