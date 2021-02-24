import sys


def print_list():
    print("1: Master of Accountancy (Online Accelerated)\n")
    print("2: Master of Business Administration\n")
    print("3: Concentration of Accounting, Master of Business Administration (online accelerated)\n")
    print("4: Concentration of Information System, Master of Business Administration (online accelerated)\n")
    print("5: Concentration of Marketing, Master of Business Administration (online accelerated)\n")
    print("6: Master of Business Administration (Online Accelerated)\n")
    print("7: Dual Degree: Master of Science (Information Technology) & Master of Business Administration\n")
    print("8: Master of Science (Information Technology)\n\n")


def option_list():
    print("1: program list\n\n")
    print("2: select program\n\n")
    print("3: quit\n\n")
    operate = input("enter the initial number to select: ")
    if operate == '1':
        print_list()
        loop()
    elif operate == '2':
        select_list()
    elif operate == '3':
        sys.exit()
    else:
        print("This option is not valid\n")
        option_list()


def select_list():
    print_list()
    choice = input("enter the initial number to see the details: ")
    return choice


def loop():
    go_back = input("1: menu\t\t2: select program\t\t3:quit\n")
    if go_back == '1':
        option_list()
        print("\n")
    elif go_back == '2':
        select_list()
        print("\n")
    elif go_back == '3':
        sys.exit()
    else:
        print("this is not a valid option")
        loop()


option_list()
