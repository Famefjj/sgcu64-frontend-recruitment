def check_out(phone_number):
    for place in checkin_dict:
        if phone_number in checkin_dict[place]:
            checkin_dict[place].remove(phone_number)

def check_in():
    
    # line indicate end of main menu section
    print("-----------------------------------------------------------------")
    print("Check in")

    # get phone number
    phone_number = input("Enter phone number: ")

    # get location of user
    places = {}

    # display check in information 
    i = 1
    for place in checkin_dict:
        print("  "+str(i)+". "+place)
        places[str(i)] = place
        i += 1
    place_input = input("Select the place: ")

    # check if input is valid. if not, try again
    if places.get(place_input, 0) == 0:
        print("invalid input, please try again")
        check_in()
    else:
        # create variable key which is place
        key = places[place_input]

        # checkout this person from other place
        check_out(phone_number)

        # append phone number
        checkin_dict[key].append(phone_number)
        
        # display check in information in user screen
        print("Check in {} into {}".format(phone_number, key))


def main():
    # create main menu
    print("Available commands:")
    print("  1. Check in user")
    print("  2. Check out user")
    print("  3. Print people count")

    # input string
    main_input = input("Please input any number: ")

    # check to see if input valid, if input not valid, try again
    if main_input == "1":
        check_in()
    elif main_input == "2":
        phone_number = input("Enter phone number you want to check out: ")
        check_out(phone_number)
    elif main_input == "3":
        pass
    else :
        print("invalid input, please try again.")
        print("-----------------------------------------------------------------")
        main()


# initialize dictionary
# use place as key and list of phone number as value
checkin_dict = {
    "Mahamakut Building" : [],
    "Sara Phra Kaew" : [],
    "CU Sport Complex": [],
    "Sanum Juub": [],
    "Samyan Mitr Town" : []
}


main()