#Ian Esser
#10/15/2021
#Module for desserts

def dessert_function():
    while True: #Runs the program again if the user enters incorrect data
        try: #Handles errors
            desserts = int(input("How many desserts are you getting?")) #Gets the number of desserts
            cost = float(input("How much does each cost?")) #Gets the cost of desserts
        except ValueError:
            print("Please make sure you entered a number.") #Displays the error message
        else:
            return desserts * cost #Returns the total cost of the desserts