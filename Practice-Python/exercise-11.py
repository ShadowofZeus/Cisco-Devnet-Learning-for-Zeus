"""
Lessons Learnt
Functions!!
Conditionals and List Iterations
"""
def input_value():
    value=int(input("Kindly enter a sample number: "))

    precheck(value)               #doing prechecks on provided number

def welcome():
    return(print("Welcome to Shadow's Coding Studio"))

def precheck(odd_prime):

    if (odd_prime>1):
        if odd_prime==2:
            print("Two is the first prime number")


        elif(odd_prime%2==0):
            print("this is an even number sir/madam")


        else:
            prime_test(odd_prime)

    else:
        print("we dont test with zeros and negative numbers here")


def prime_test(prime_odd):

    prime_list=[3,5,7,11,13,17,19,23]

    for each_num in prime_list:                     #dividing my input with the list
        if prime_odd==each_num:
            flag=1
            flag_result(flag)
            break

        elif prime_odd%each_num==0:
            flag=0
            flag_result(flag)
            break

        else:
            flag=1
            flag_result(flag)
            break


        return flag

def flag_result(flag_value):

    if flag_value==1:
        print("This is a prime number")

    else:
        print("This is not a prime number")

################## $$$$$$$$################ $$$$$$$$$$ ###################

welcome()
input_value()
