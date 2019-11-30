"""
Sets
Functions
"""

def clean_duplicates(sample_list):

    cleanlist=set(sample_list)
    print("List after duplicate cleaning:")
    print(cleanlist)


def get_values():

    capture_list=[]
    size_of_list=int(input("Enter a number for the list size: "))

    for i in range(1,size_of_list+1):               # new for me!!
        capture_var=int(input("Enter a number for your list: "))
        capture_list.append(capture_var)

    print("List before cleaning:")
    print(capture_list)
    clean_duplicates(capture_list)


get_values()
