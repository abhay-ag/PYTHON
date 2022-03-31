from time import sleep


userArray = []
passArray = []
balance = [0] * 9999
def start():
    choice = ''
    i = 0
    while choice != 'l' and choice != 'c' and choice != 'q':
        choice = input("\nChoose from the options below\n\tl -> login\n\tc -> create an account \n\tq -> quit\n\n> ")
        if ( i== 3):
            exit(0)
        i += 1
        
    if choice == "l":
        login()
    elif choice == "c":
        createAccount()
    elif choice == "q":
        exit(0)

def login():
    global user, paswd
    if (len(userArray) == 0 and len(passArray) == 0):
        print("\nCurrently we have no accounts! Please register first!!")
        start()
    else:
        user = input("\n\nEnter your username: ")
        if(not(user in userArray)):
            print("\nNo such user exists! Please register first!!")
            start()
        else:
            paswd = input("\nEnter your password: ")
            if(paswd == passArray[userArray.index(user)]):
                print("\n****LOGIN SUCCESSFUL****")
                printMainMenu(user)
            else:
                print("\nWRONG PASSWORD! Please start again")
                start()


def createAccount():
    user = input("\nPlease enter your User Name: ")
    paswd = input("\nPlease enter a Password: ")

    userArray.append(user)
    passArray.append(paswd)

    start()

def printMainMenu(username):
    print("\nWelcome, ",username,"! Please choose from below")
    i = 0
    choice = ''
    while choice != 'd' and choice != 'w' and choice != 'r' and choice !='q':
        choice = input("\n\td -> deposit money\n\tw -> withdraw money\n\tr -> request balance\n\tq -> quit\n\n> ")
        if i == 2:
            print("\nInvalid input received too many times exiting ....")
            sleep(2)
            start()

    if choice == 'd':
        deposit(username)
    elif choice == 'w':
        withdraw(username)
    
def deposit(username):
    bal = int(input("\nEnter the amount to be deopited: "))
    balance[userArray.index(username)] += bal
    sleep(1)
    print("\nTRANSACTION SUCCESSFUL")
    sleep(1)
    printMainMenu(username)

def withdraw(username):
    if(balance[userArray.index(username)] == 0):
        print("\nYou have 0 balance! Please deposit some money first.")
        sleep(1)
        printMainMenu(username)
    else:
        withMoney = int(input("\nEnter the amount to be withdrawn: "))
        if(withMoney > balance[userArray.index(username)]):
                print("\nInsufficient balance in your account! Please try again!!")
                sleep(1)
                printMainMenu(username)
        else:
            balance[userArray.index(username)] -= withMoney
            sleep(1)
            print("\nTRANSACTION SUCCESSFUL")
            sleep(1)
            printMainMenu(username)




print("\nWelcome to the ATM Project\n")
start()