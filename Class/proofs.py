"""
Python Crash Course
By Eric Matthes

Exercise proofs
"""

# Exercise 9-10 proof
from imported_restaurant import Restaurant as res

burger_house = res('burger house', 'burger')
burger_house.describe_restaurant()

# End of exercise 9-10

# Exercise 9-11 proof
from imported_admin import Admin

admin = Admin('sijan', 'shrestha', 'sijan97', 'sijan@example.com', 'kathmandu')

admin.privileges.show_privileges()

print("\nAdding privileges...")

admin_privileges = ['can add post', 'can delete post', 'can ban users']
admin.privileges.privileges = admin_privileges

admin.privileges.show_privileges()

# End of exercise 9-11