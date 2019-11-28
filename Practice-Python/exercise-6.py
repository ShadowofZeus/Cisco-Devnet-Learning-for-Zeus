"""
Learning Points for me:
#Palindromes
To reverse a string using slicing, write:

stringname[stringlength::-1] # method 1 : String Slicing :  means start at string length, end at position 0, move with the step -1 (or one step backward).
"""

word_string=str(input("Enter a word to check if its a palindrome: "))
str_len=len(word_string)
rvrsd_string = word_string[str_len::-1]
# print(rvrsd_string)            #Checking if string is reversed

if word_string==rvrsd_string:
    print("this is a Palindrome")

else:
    print("its not a palindrome baba!")
