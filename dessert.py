#Ian Esser
#10/15/2021
#Module for desserts

def dessert_function():
    while True:
        try:
            desserts = int(input("How many desserts are you getting?"))
            cost = float(input("How much does each cost?"))
        except ValueError:
            print("Please make sure you entered a number.")
        else:
            return desserts * cost