"""
Learning Outcomes:
-> While loops
-> Infinite loops
-> Break statements
"""
print("*********** MENU ***************")
print("Welcome to Rock, Paper , scissors \n")
print("Please select the below options:\n")
print("Select \n 'r' for Rock \n 's' for Scissors \n 'p' for Paper \n 'q' to exit program")
print("Kindly input character only and do not include the quotes \n")

play1=str(input("Please enter option for player-1: "))
play2=str(input("Please enter option for player-2: "))

while 1:
    if play1=='q' or play2 =='q':
        print("Exitting System")      #Check
        break
    elif play1=='r' and play2 =='r':
        print("Its a tie")
        break
    elif play1=='p' and play2 =='p':
        print("Its a tie")
        break
    elif play1=='s' and play2 =='s':
        print("Its a tie")
        break
        #loop to start again
        #print("Second phase")       - Check
        break
    elif play1=='r' and play2 =='p':
        print("Paper wraps rock")
        print("Player 2 wins")
        break
    elif play1=='p' and play2 =='s':
        print("Player 2 wins")
        break
    elif play1=='s' and play2 =='r':
        print("Player 2 wins")
        break
    elif play1=='r' and play2 =='s':
        print("Player 1 wins")
        break
    elif play1=='p' and play2 =='r':
        print("Player 1 wins")
        break
    elif play1=='s' and play2 =='p':
        print("Player 1 wins")
        break
    else:
        print("invalid input - Please try again")
        break
