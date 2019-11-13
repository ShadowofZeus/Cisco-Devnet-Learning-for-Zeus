""""
This is the print lists function which prints the contents of any list
"""

def print_lists(AnyList,level=0):
    for each_item in AnyList:
        if isinstance(each_item,list):
            print_lists(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end="")
                print(each_item)
