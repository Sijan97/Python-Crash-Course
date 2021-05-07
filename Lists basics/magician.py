"""
Python Crash Course 
By Eric Matthes

Tutorial: List and Loop

"""

#Creating a list
magicians = ['alice', 'david', 'dynamo', 'chris']
#Note: magician is a temporary variable used to hold values of the list
#Note: Common mistake made during looping is to forget the colon.
for magician in magicians:
	print(f"{magician.title()} performed a great trick.")
	print(f"I can't wait to see your next trick, {magician.title()}.\n")

"""
Every line of code inside the for loop indentation is associated with for loop
and repeat till the end of the loop. The line below is written outside the for
loop indentation and hence will be printed only once.

"""
print("Thank you for a great show!!!")