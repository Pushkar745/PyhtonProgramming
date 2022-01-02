# The raise statement allows the programmer to force a specific exception to occur.

# Program to depict Raising Exception
try:
    raise NameError("Hi There ")  # Raise Error
except NameError:
    print("An exception")
    raise  # To dertemine whether the exception was raised or not
