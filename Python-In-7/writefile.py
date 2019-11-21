#Supeeeerrr Cooollll!!!
"""
file_input = open("motivation.txt",'w')
file_input.write("Never give up")
file_input.write("\nRise above hate")
file_input.write("\nNo body remember second place")
file_input.close()
"""

#Write the file without clobbering it(Overwriting it)
file_input = open("newmotivation.txt",'a')
file_input.write("Never give up")
file_input.write("\nRise above hate")
file_input.write("\nNo body remember second place")
file_input.close()

# then add more quotes

file_input = open("newmotivation.txt",'a')
file_input.write("\nBlood sweat and respect")
file_input.write("\nThe first two you give")
file_input.write("\nThe last you earn")
file_input.write("\nGive it Earn it")
file_input.close()
