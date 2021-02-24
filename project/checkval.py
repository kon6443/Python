import introduction
import userManual

import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


### def select_list(): #this function should overlap with Hao Lan's code
###    choice = int(input("Please enter the number corresponding to the degree you wish to see: "))
###    return choice

def printout():
    choice = userManual.select_list()   #assign returned value to choice
    
    file = open(resource_path("masters.txt"), "r")
    content = file.readlines()
  
    if choice == 1:
        print(content[5:30])

    elif choice == 2:
        print(content[32:57])

    elif choice == 3:
        print(content[59:82])

    elif choice == 4:
        print(content[84:103])
    
    elif choice == 5:
        print(content[105:124])

    elif choice == 6:   
        print(content[126:145])
    
    elif choice == 7:
        print(content[147:169])

    elif choice == 8:
        print(content[171:196])

    else:
        print("Incorrect entry.")
    repeat()

def repeat():
    userInput = input("Would you like to view another program?(enter y or n) ")
    if userInput == 'y':
        printout()

    elif userInput == 'n':
        print("Have a good day!")

printout()