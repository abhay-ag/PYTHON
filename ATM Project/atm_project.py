userArray = []
passArray = []
balance = [0] * 9999
def start():
    print("Welcome to the ATM Project\n\n")
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
        if(not(userArray.index(user))):
            print("\nNo such user exists! Please register first!!")
        else:
            paswd = input("\nEnter your password: ")
            if(paswd == passArray[userArray.index(user)]):
                print("\n****\tLOGIN SUCCESSFUL\t****")
            else:
                print("\nWRONG PASSWORD! Please start again")


def createAccount():
    user = input("\nPlease enter your User Name: ")

start()