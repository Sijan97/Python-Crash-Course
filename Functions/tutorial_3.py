"""Python Crash Course 
By Eric Matthes

Tutorial: Return values"""

# Formatted name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Assigning return value to a variable
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Making an argument optional.
def get_name(first_name, last_name, middle_name=''):
    """Return a neatly formatted name."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

# Calling the function
musician = get_name('jimi', 'hendrix')
father = get_name('santosh', 'shrestha', 'lal')
print("\n" + musician)
print("\n" + father)

# Returning a dictionary
def person_details(first_name, last_name, information):
    """Returning a dictionary of information about a person."""
    person = {'fname': first_name, 'lname': last_name, 'info': information}
    return person

# Calling the function
musician = person_details('jimi', 'hendrix', 'musician')
print(f"\n{musician}")

# Adding another special parameter
def build_person(first_name, last_name, age=None):
    """Returns a dictionary of information about a person."""
    person = {'fname': first_name, 'lname': last_name}
    if age:
        person['age'] = age    # Stores nothing or None value to dictionary.
    return person

musician = build_person('jimi', 'hendrix', 27)
print(f"\n{musician}")
actor = build_person('keanu', 'reeves')
print(f"\n{actor}")

# Using a function with while loop
def get_name(first_name, last_name):
    """Returns a neatly formatted full name."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nWhat is your name?")
    print("(Enter 'q' to quit)")
    fname = input("First name: ")
    if fname == 'q':
        break

    lname = input("Last name: ")
    if lname == 'q':
        break

    formatted_name = get_name(fname, lname)
    print(f"\nHello, {formatted_name}!")
