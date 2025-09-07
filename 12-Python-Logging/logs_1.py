import logging

# Configure basic logging to print messages to the console
logging.basicConfig(level=logging.DEBUG)

# Log some informational messages
logging.info("Program started.")


logging.debug(f"This will only print when the log level is debug")

name = "Alice"
age = 30
logging.info(f"User: {name}, Age: {age}")

result = 10 + 5
logging.info(f"The result of the addition is: {result}")

logging.warning("Program finished.")
