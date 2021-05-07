"""
Python Crash Course
By Eric Matthes

Exercise: 11-3
"""

class Employee:
    """Stores employee details and gives annual raise."""
    def __init__(self, first_name, last_name, annual_salary):
        """Initializes employee details."""
        self.fname = first_name
        self.lname = last_name
        self.salary = annual_salary
        self.annual_raise = 0

    def give_raise(self, annual_raise=5000):
        """Gives annual raise to employee."""
        self.annual_raise = annual_raise

    def emp_det(self):
        """Shows employee details."""
        print("Employee detail:")
        print(f"\tFull name: {self.fname.title()} {self.lname.title()}")
        print(f"\tAnnual salary: {self.salary}")
        print(f"\tAnnual raise: {self.annual_raise}")