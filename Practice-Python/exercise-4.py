"""
Lessons Learnt
Range command
Conditionals and Lists
"""

extent=int(input("Kindly enter a smaple number: "))
listbaba=range(1,extent+1)               # range command is Powerfull!!

for item in listbaba:
    if (extent%item==0):
        print(item)

    else:
        pass
