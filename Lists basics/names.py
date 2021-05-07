"""
Python Crash Course
By Eric Matthes

"""
#List basics
friends = ["rumi", "sajik", "nishan", "rohit", "sanam", "pemba"]
message1 = f"{friends[0].title()} is the love of my life."
message2 = f"{friends[1].title()}, {friends[2].title()}, {friends[3].title()} and {friends[4].title()} are my childhood friends."
message3 = f"{friends[-1].title()} is my best college friend."
print(f"Who my friends are:\n\t{message1}\n\t{message2}\n\t{message3}")