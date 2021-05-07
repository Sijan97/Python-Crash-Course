"""
Python Crash Course
By Eric Matthes

Tutorial: Class testing
"""

class AnonymousSurvey:
    """Collects anonymous answers to a survey question."""

    def __init__(self, question):
        """Store question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Shows question for the survey."""
        print(self.question)

    def store_response(self, new_response):
        """Stores response to the question."""
        self.responses.append(new_response)

    def show_result(self):
        """Shows the survey result."""
        print("\nSurvey result:")

        for response in self.responses:
            print(f"- {response}")