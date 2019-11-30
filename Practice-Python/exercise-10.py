import random

"""
List Comprehensions:
syntax:
[ expression for item in list if conditional ]
is the same as:
for item in list:
    if conditional:
        expression
Random generators : random module
"""
a_list=random.sample(range(15), 7)            #in a range of 0-15 , generate only 7 numbers
b_list = random.sample(range(10), 10)
newlist=[]

customlist = [newlist.append(b) for a in a_list for b in b_list if a==b]
print(a_list)           #to check if program is accurate
print(b_list)
print(newlist)
