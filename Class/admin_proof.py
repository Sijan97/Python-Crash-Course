"""
Python Crash Course
By Eric Matthes

Exercise 9-12 proof
"""

from admin import Admin

new_admin = Admin('eric', 'matthes', 'emat27', 'emat@example.com', 'texas')
new_admin.privileges.show_privileges()

print("\nAdding privileges...")

admin_privileges = ['can add post', 'can delete post', 'can ban users']
new_admin.privileges.privileges = admin_privileges
new_admin.privileges.show_privileges()

# End of exercise 9-12