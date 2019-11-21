"""  OPTION 1
file_input = open("sample1.txt",'r')        # file_input object created for open file
all_read = file_input.read()                #read method used on open file_input object
print(all_read)                             #print all that is read
file_input.close()                          #always close file after use
"""

#OPTION 2  - WAY much neater and it works
file_input = open("sample1.txt",'r')
for line in file_input:
    print(line)

file_input.close()
