import random
import sys

#a = random.randint(2, 6)            #variable a will have a random integer that the computer made for you, between 2 and 6 (including 2 and 6).

def comparison(gvalue,rand_gen):

    gvalue_int=int(gvalue)

    if gvalue_int==rand_gen:
        return("You are a star - You guessed the generated value")

    elif gvalue_int>rand_gen:
        return("You guessed a larger value that wat was generated")

    else:
        return("You guessed a lower value than what was generated")

count=int(0)                    # count has to be outside so that it is not re-initialized to zero ALWAYS

while 1:

    rand_nmbr=random.randint(1, 9)
    print("Generated Number: %d" %(rand_nmbr))         #Check if program is accurated
    print("Guessing Attempts: %d" %(count))
    print("Type 'exit' to leave the program")
    guess=input("Guess a number between 1 and 9: ")


    if guess=='exit':
        print("Exitting the System")
        sys.exit()

    elif guess=='1' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='2' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='3' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='4' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='5' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='6' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='7' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='8' :
        print(comparison(guess,rand_nmbr))
        count+=count

    elif guess=='9' :
        print(comparison(guess,rand_nmbr))
        count+=count

    else:
        print("invalid Input, please follow instructions and TRy again")
