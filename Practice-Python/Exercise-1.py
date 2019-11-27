from datetime import datetime

"""
Concepts for this week:

1.Getting user input
2.Manipulating strings (a few ways)
"""

name =input("Enter your name: ")
age = int(input("Enter your age: "))
currentYear = datetime.now().year
addyears = int(100-age)
repeat = int(input("Enter the number of times to print out: "))



#print("Your name is " +name +" and your age is "+age)  OR

#print("Your name is " +name +" and your age is "+str(age)) OR

print("Your name is %s and your age is %d" %(name,age))    # The approach I like
#print("the year is %d" %(currentYear))     just to confirm if datetime library is working

# print("you will get to hundred in year %d" %(addyears+currentYear))

print(repeat * ("you will get to hundred in year %d \n" %(addyears+currentYear)))
