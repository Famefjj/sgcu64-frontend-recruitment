
def check_in():
    
    # line indicate end of main menu section
    print("-----------------------------------------------------------------")

    print("Check in")

    # get phone number
    phone_number = input("Enter phone number: ")

    # get location of user
    places = {
        "1":"Mahamakut Building",
        "2":"Sara Phra Kaew",
        "3":"CU Sport Complex",
        "4":"Sanum Juub",
        "5":"Samyan Mitr Town"
    }

    # display check in information 
    for key in places:
        print("  "+key+". "+places[key])
    place_input = input("Select the place: ")

    
    # check if input is valid. if not, try again
    if places.get(place_input, 0) == 0:
        print("invalid input, please try again")
        check_in()
    else:
        # create variable key which is place
        key = places[place_input]

        # checkout this person from other place
        

        # check to see if this place is added
        if checkin_dict.get(key, 0) == 0:
            checkin_dict[key] = []
            
        # append phone number
        checkin_dict[key].append(phone_number)

        print(checkin_dict)
        
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
        pass
    elif main_input == "3":
        pass
    else :
        print("invalid input, please try again.")
        print("-----------------------------------------------------------------")
        main()


# initialize dictionary
# use place as key and list of phone number as value
checkin_dict = {}

while True:
    main()