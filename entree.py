#Ian Esser
#10/15/2021
#Module for entrees

def entree_function():
    while True: #Runs the program again if the user enters incorrect data
        try: #Handles errors
            entrees = int(input("How many entrees are you getting?")) #Gets the number of entrees
            cost = float(input("How much does each cost?")) #Gets the cost of entrees
        except ValueError:
            print("Make sure you entered a number.") #Displays the error message
        else:
            return entrees * cost #Returns the total cost of the entrees