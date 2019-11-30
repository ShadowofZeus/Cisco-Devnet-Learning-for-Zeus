"""
Learning Outcomes:
List properties
Functions
"""

def welcome():
    return(print("Welcome to Shadow's Coding Studio"))

def get_values():

    capture_list=[]
    size_of_list=int(input("Enter a number for the list size: "))

    for i in range(1,size_of_list+1):               # new for me!!
        capture_var=int(input("Enter a number for your list: "))
        capture_list.append(capture_var)

    print(capture_list)
    list_ends(capture_list)

def list_ends(list_racho):

    newlist=[]
    newlist.append(list_racho[0])
    newlist.append(list_racho[-1])

    print(newlist)

####################### $$$$$$$$$$$$$$$$$$$ @@@@@@@@@@@@@@@@ #########################
welcome()
get_values()
