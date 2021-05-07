"""Python Crash Course
By Eric Matthes

Exercises: 8-9 to 8-11"""

# Exercise 8-9
# Messages
def show_messages(messages):
    """Displaying short messages"""
    print("")
    for message in messages:
        print(message.title())

messages = ['save earth', 'i love python', 'hello world!']
show_messages(messages)

# End of exercise 8-9

# Exercise 8-10 (Non-book version)
# Sending messages
# def send_messages(messages):
#     """Printing message and moving printed message to sent_messages."""
#     sent_messages = []
#     while messages:
#         to_send = messages.pop()
#         add_message = to_send + ' python'
#         sent_messages.append(add_message)

#     for sent_message in sent_messages:
#         messages.append(sent_message)

# messages = ['hello', 'save', 'i love']

# show_messages(messages)
# send_messages(messages)
# show_messages(messages)

# End of exercise 8-10

# Exercise 8-10 (Book version)
def send_messages(messages):
    """Printing message and moving printed message to sent_messages."""
    sent_messages = []
    print("\nOngoing messages:")
    while messages:
        to_send = messages.pop()
        print(F"Sending message: {to_send.title()}")
        sent_messages.append(to_send)

    print("\nSent Messages:")
    for sent_message in sent_messages:
        print(sent_message.title())

messages = ['hello python!', 'save world', 'i love earth']

show_messages(messages)
send_messages(messages)

# End of exercise 8-10