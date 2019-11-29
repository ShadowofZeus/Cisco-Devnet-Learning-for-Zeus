import os

os.chdir("C:/Users/masa656/github/Cisco-Devnet-Learning-for-Zeus")

print("Directory changed")

"""
data = open('sketch.txt')
print(data.readline(), end='')

data.seek(0)                      #Return to the beginning of the file
for each_line in data:              #iterate your reading of the file
        print(each_line, end='')


data.close()                      #always close a file after reading it
print("\n"+"File Closed Simz")
"""

""""""""""""""""""""""""""""
Code with Exception Handling
""""""""""""""""""""""""""""

try:
    data = open('sketch.txt')

for each_line in data:
    try:
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print(' said: ', end='')
        print(line_spoken, end='')

    except ValueError:
        pass
            data.close()
            except IOError:
            print('The data file is missing!')
