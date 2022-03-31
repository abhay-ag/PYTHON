def start():
    print("Welcome to the ATM Project\n\n")
    choice = ''
    i = 0
    while choice != 'l' and choice != 'c' and choice != 'q':
        choice = input("Choose from the options below\n\tl -> login\n\tc -> create an account \n\tq -> quit\n\n>")
        if ( i== 3):
            exit(0)
        i += 1
        