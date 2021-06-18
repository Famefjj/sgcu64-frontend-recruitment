
# get and check input in main menu page
def main_input_check():
    main_input = input("Please input any number: ")

    # check to see if input valid, if input not valid, try again
    if main_input == "1":
        print("valid")
    elif main_input == "2":
        pass
    elif main_input == "3":
        pass
    else :
        print("input incorrect, please try again.")
        main_input_check()


def main():
    # create main menu
    print("Available commands:")
    print("  1. Check in user")
    print("  2. Check out user")
    print("  3. Print people count")
    main_input_check()
    
main()