# Programmer: David Yue
# Date: 10/14/21
# Module for appitizer


def appitizer_function():
    while True: # Allow the user to try again
        try:  # In case the user types with letters
            people = int(input("How many people are getting appitizers?"))
            price = float(input("How much do each cost?"))
        except ValueError:
            print("please type in numbers not letters")
        else:
            return people * price  # This will calculate total








