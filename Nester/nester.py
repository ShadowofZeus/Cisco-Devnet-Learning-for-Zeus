""""
This is the print lists function which prints the contents of any list
"""

def print_lists(AnyList,level=0,indent=False,fh=sys.stdout):
    for each_item in AnyList:
        if isinstance(each_item,list):
            print_lists(each_item,level+1,indent,fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="",file=fh)
                    print(each_item,file=fh)
