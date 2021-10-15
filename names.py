#Ian Esser
#10/8/2021
#Name Counter

#Main function - Calls the nameCounter function
def main():
    nameCounter()

#Counts the number of names in the list
def nameCounter():
    try:
        names = open("names.txt", "r") #Opens the names.txt file and assigns it to names
    except IOError:
        exit("The file could not be found.") #Displays an error that tells the user what went wrong
    namesList = names.readlines() #Converts names.txt into a list
    length = len(namesList) #Sets the length of the list to the variable length
    names.close() #Closes the file
    print(f"\nThere are {length} names in this file.") #Prints the number of lines in the file

#Calls the main function
if __name__ == "__main__":
    main()