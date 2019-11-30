"""
Learning Outcomes
Lists
Functions
Fibonacci  numbers!!
"""

def welcome():
    return(print("Welcome to Shadow's Coding Studio"))

def get_values():

    capture_list=[1,1]
    size_of_list=int(input("How many Fibonacci's to generate: "))
    n=2
    for i in range(1,size_of_list-1):

        capture_list.append(capture_list[n-1]+capture_list[n-2])

        n=n+1                                             #increment your counter for every cycle

    print(capture_list)

####################### $$$$$$$$$$$$$$$$$$$ @@@@@@@@@@@@@@@@ #########################
welcome()
get_values()
