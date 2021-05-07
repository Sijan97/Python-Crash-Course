"""
Python Crash Course
By Eric Matthes

Tutorial: Testing
"""

from survey import AnonymousSurvey

# Define a question and make a survey.
question = "What is your favorite language?"
my_survey = AnonymousSurvey(question)

# Show question, and store the responses.
my_survey.show_question()
print("Enter 'q' anytime to quit.")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show survey results.
print("Thank you everyone for participating in the survey!")s
my_survey.show_result()