#!/usr/bin/python

import random
import string

def strongpassgenerator(password_length=12):

    alphanum = string.ascii_letters + string.digits
    return ''.join(random.choice(alphanum) for i in range(password_length))



print ("Kindly enter the password length to be generated")
pass_length=int(input("I will not allow a value less than 12 please: "))
print ("Your generated password is:   ", strongpassgenerator(pass_length))
