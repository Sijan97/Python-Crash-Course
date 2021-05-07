"""
Python Crash Course
By Eric Matthes

Tutorial: Testing
"""

import unittest
from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey"""
#     def test_store_single_response(self):
#         """Tests that a single response can be stored properly"""
#         question = "What is your favorite language?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response("English")
#         self.assertIn("English", my_survey.responses)

#     def test_store_multiple_responses(self):
#         """Tests that multiple responses can be stored properly"""
#         question = "What is your favorite language?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Mandarin', 'Spanish']
#         for response in responses:
#             my_survey.store_response(response)

#         for response in responses:
#             self.assertIn(response, my_survey.responses)

# if __name__ == '__main__':
#     unittest.main()

# The setUp() method
# In above solution we created similar responses twice,
# the setUp() method helps to create responses once and use it multiple times.
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    def setUp(self):
        """Create survey and responses for use in all test cases."""
        question = "What is your favorite language?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Mandarin', 'Spanish']
    
    def test_store_single_response(self):
        """Tests that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_multiple_responses(self):
        """Tests that multitple responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()        