""""
This is the print lists function which prints the contents of any list
"""

def print_lists(AnyList):
    for each_item in AnyList:
        if isinstance(each_item,list):
            print_lists(each_item)
        else:
            print(each_item)

print_lists(movies)
