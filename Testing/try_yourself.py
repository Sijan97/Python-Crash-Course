"""
Python Crash Course
By Eric Matthes

Exercises: 11-1 to 11-2
"""

# Exercise 11-1 and 11-2
# City, Country
import unittest
from city_functions import city_country

class CityNamesTestCase(unittest.TestCase):
    """Tests city_function.py"""
    def test_city_country(self):
        """Do information like 'Santiago, Chile' work?"""
        city_detail = city_country('santiago', 'chile')
        self.assertEqual(city_detail, 'Santiago, Chile')

    def test_city_country_population(self):
        """Can I add population?"""
        city_detail = city_country('santiago', 'chile', population=50000)
        self.assertEqual(city_detail, 'Santiago, Chile - population 50000')

if __name__ == '__main__':
    unittest.main()

# End of exercise