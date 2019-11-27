"""
Concepts for this week:

Modular arithmetic (the modulus operator)
Conditionals (if statements)
Checking equality
"""

sampleN=int(input("Enter integer number: "))
mod_two=sampleN%2
mod_four=sampleN%4

if mod_four==0:
    print("this is a multiple of four")

elif mod_two==0:
    print("this is an even number")

else:
    print("this is an ODD number")
