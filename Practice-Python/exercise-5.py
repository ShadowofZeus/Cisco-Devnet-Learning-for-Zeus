"""
Learning points for me:
Lists and sets(unique elements)
random.randint(a, b)
"""
a_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list=[]
#overlap=int(input("Enter a number between 1 and 13: "))
print("Intersecting Numbers are:")

for item_a in a_list:
        if item_a in b_list:
            #print(item_a)             to check what is being printed out
            new_list.append(item_a)

        else:
            pass
new_set=set(new_list)
print(new_set)
