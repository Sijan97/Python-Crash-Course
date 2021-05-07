"""Python Crash Course
By Eric Matthes

Tutorial: Functions and aruguments"""

# Positional arguments
# Pets
def pet(animal_type, pet_name):
    """Display information about pet."""
    print(f"{pet_name.title()} is a good {animal_type}.")

# Calling the function
pet('dog', 'pintu')

# Multitple function calling
pet('cat', 'snow')
pet('mouse', 'stuart')

# Note: Order matters in positional arguments.

# Keyword arguments
def pet_info(animal_type, pet_name):
    """Display information about pet."""
    print(f"\nI have a pet {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Calling the function
pet_info(animal_type = 'dog', pet_name = 'pintu')
pet_info(pet_name='stuart', animal_type='mouse')

# Note: Order does not matter in keyword arguments.
# But, name of the parameter must match during function call.

# Default values
# When writing a function, we can define a default value for each parameter.
def describe_pet(pet_name, animal_type='dog'):
    """Display information about pet."""
    print(f"\nI have a pet {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Calling the function
describe_pet(pet_name='pintu')

# Since one parameter has default value, only one argument can be passed.
describe_pet('tommy')

# We can explicitly change the default argument during function call.
describe_pet(pet_name='snow', animal_type='cat')

# Note: Default argument parameters must always be positioned at last.

# All these function calls are valid and equivalent.
describe_pet('pintu')
describe_pet(pet_name='pintu')

describe_pet(pet_name='snow', animal_type='cat')
describe_pet('snow','cat')
describe_pet(animal_type='cat', pet_name='snow')