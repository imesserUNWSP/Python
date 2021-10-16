#Ian Esser
#10/15/2021
#Module for entrees

def entree_function():
    while True:
        try:
            entrees = int(input("How many entrees are you getting?"))
            cost = float(input("How much does each cost?"))
        except ValueError:
            print("Make sure you entered a number.")
        else:
            return entrees * cost