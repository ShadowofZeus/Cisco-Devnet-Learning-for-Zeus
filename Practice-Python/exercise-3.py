"""
Lists
More conditionals (if statements)
"""

cap=int(input("Enter nummber to cap list: "))
listbaba = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist=[]

for item in listbaba:
    if item<cap:
        newlist.append(item)

for new_item in newlist:
    print(new_item)
