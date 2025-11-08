import greetings # Use the module
import sys
import json

# To load modules from different locations
sys.path.append('/C:/Desktop/python-data-engineer-main')

message_hello = greetings.say_hello("Alice")

message_goodbye = greetings.say_goodbye("Bob")
print(message_hello)
print(message_goodbye)

#print(message) # Output: Hello, Alice!
