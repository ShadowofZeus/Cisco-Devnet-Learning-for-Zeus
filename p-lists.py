movies=["The Holy Grail","The Life of Brian","The Meaning of Life"]
movies.insert(1,1973)
movies.insert(3,1992)
movies.append(1834)

"""
count=0                    #printing list contents dynamically
while count<len(movies):
    print(movies[count])
    count=count+1
"""
"""
for each_item in movies:    #//printing list contents dynamically
    print(each_item)
"""

movies = [
    "The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
        ["Graham Chapman",
                ["Michael Palin", "John Cleese", "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

""""
for each_item in movies:
    if isinstance(each_item, list):
        for nested_item in each_item:
            if isinstance(nested_item, list):
                for deeper_item in nested_item:
                    print(deeper_item)
            else:
                print(nested_item)
    else:
        print(each_item)
"""

def print_lists(AnyList):
    for each_item in AnyList:
        if isinstance(each_item,list):
            print_lists(each_item)
        else:
            print(each_item)

print_lists(movies)
