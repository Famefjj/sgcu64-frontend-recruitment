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


# main function
def main():
    input_time = input().strip()
    
    # check input format
    if input_check(input_time):
        print("okay")
    else:
        print("error")
        


# initialize main function      
main()



    



