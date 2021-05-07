"""Python Crash Course 
By Eric Matthes

Tutorial: List in functions"""

# Passing a list in function
def greet_users(usernames):
    """Print a simple greeting message to users."""
    for user in usernames:
        print(f"Hello, {user.title()}!\n")

greet_users(['sijan', 'rumi', 'pemba'])

# Modifying a list in a function
# A simple program that designs 3d model
ordered_models = ['robot', 'wasp', 'ant']
completed_models = []

while ordered_models:
    on_progress = ordered_models.pop()
    print(f"Printing model: {on_progress.title()}")
    completed_models.append(on_progress)

print("\nCompleted models:")
for model in completed_models:
    print(f"{model.title()}")

# Defining 2 different functions to design the model and display the completed.
def design_models(incomplete_models, completed_orders):
    """Designing incomplete models and moving to completed_orders"""
    print("\nPrinting in progress:")
    while incomplete_models:
        on_progress = incomplete_models.pop()
        print(f"\tPrinting model: {on_progress.title()}")
        completed_orders.append(on_progress)

def display_models(completed_orders):
    """Displays completed orders"""
    print("\nOrders completed:")
    for model in completed_orders:
        print(f"\t{model.title()}")

# Calling functions
incomplete = ['bear', 'teeth', 'bottle']
completed = []
design_models(incomplete, completed)
display_models(completed)

# Preventing a function from modifying a list
# Send the copy of the original list to the function parameter to prevent
# from losing all the items in the list using slice.

to_print = ['car', 'truck', 'plane']
printed = []

# Using slice to send the copy during function call
design_models(to_print[:], printed)
display_models(printed)

# Lets see if the list is preserved
print(f"\n{to_print}")

# As you can see the original list is preserved.
# Note: It is often advised to use original list, unless you want a copy.