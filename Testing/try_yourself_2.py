"""
Python Crash Course
By Eric Matthes

Exercise: 11-3
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for class Employee"""
    def setUp(self):
        """Creates employee object for test cases."""
        self.my_employee = Employee('sijan', 'shrestha', 100000)

    def test_give_default_raise(self):
        """Checks if default raise amount is added successfully."""
        self.my_employee.give_raise()
        self.assertEqual(5000, self.my_employee.annual_raise)

    def test_give_custom_raise(self):
        """Checks if custom raise amount is added successfully."""
        self.my_employee.give_raise(10000)
        self.assertEqual(10000, self.my_employee.annual_raise)

if __name__ == '__main__':
    unittest.main()