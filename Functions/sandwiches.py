"""Python Crash Course
By Eric Matthes

Exercises: 8-12 to 8-14"""

# Exercise 8-12
# Sandwiches
def make_sandwiches(*types):
    """Summary of the type of sandwich requested"""
    print("\nRequested sandwich:")
    for sandwich_type in types:
        print(f"- {sandwich_type.title()}")

make_sandwiches('bacon')
make_sandwiches('ham', 'cheese')
make_sandwiches('chicken', 'cheese', 'mustard')

# End of exercise 8-12

# Exercise 8-13
# User profile
def user_profile(fname, lname, **user_info):
    """Dictionary that describes me"""
    user_info['first_name'] = fname
    user_info['last_name'] = lname
    return user_info

build_profile = user_profile('sijan', 'shrestha',
                             location='kathmandu', age=23)
print(f"\n{build_profile}")

# End of exercise 8-13

# Exercise 8-14
# Cars
def make_car(manufacturer, model_name, **car_info):
    """Make a dictionary representing a car"""
    # car_info['manufacturer'] = manufacturer.title()
    # car_info['model_name'] = model_name.title()
    # return car_info

    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model_name.title(),
        }

    for spec, detail in car_info.items():
        car_dict[spec] = detail

    return car_dict 

my_honda = make_car('honda', 'extreme', color='red', year=2002)
print(f"\n{my_honda}")

my_subaru = make_car('subaru', 'fiesta', tow_package=True, color='black')
print(my_subaru)

# End of exercise 8-14