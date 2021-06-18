import re

# function for checking input format
def input_check(input_time):

    # check length of input
    if len(input_time) != 8:
        return False

    # check pattern format
    right_pattern = re.compile(r'\d\d:\d\d:\d\d')

    if right_pattern.search(input_time):

        # if pattern format right, check number of min and sec
        hr,mi,sec = [int(e) for e in input_time.split(":")]
        if mi < 60 and sec < 60:
            return True
    
    # return False if not satisfied 2 condition above
    return False

# function for display time in screen
def display(input_time):

    display_dict = {
        "0":[" __ ","|  |","|__|"],
        "1":["    ","   |","   |"],
        "2":[" __ "," __|","|__ "],
        "3":[" __ "," __|"," __|"],
        "4":["    ","|__|","   |"],
        "5":[" __ ","|__ "," __|"],
        "6":[" __ ","|__ ","|__|"],
        "7":[" __ ","   |","   |"],
        "8":[" __ ","|__|","|__|"],
        "9":[" __ ","|__|"," __|"],
        ":":[  " " ,  "." ,  "." ],
        "e":["    ","    "," __ "]
    }

    for i in range(3):
        for e in input_time:
            print(display_dict[e][i], end=" ")
        print()


# main function
def main():
    input_time = input().strip()
    
    # check input format if input correct display xx:xx:xx else display _ _ : _ _ : _ _
    if input_check(input_time):
        display(input_time)
    else:
        display("ee:ee:ee")
        


# initialize main function      
main()



    



