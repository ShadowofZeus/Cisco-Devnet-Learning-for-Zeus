import pickle

name = ["mohit","bhaskar", "manish"]  #List
skill = ["Python", "Python", "Java"]    #list again
pickle_file = open("emp1.dat","wb")      #create file called emp1.dat and write to it in BINARY!!!!!
pickle.dump(name,pickle_file)           #store list called name in pickle_file called emp1.dat
pickle.dump(skill,pickle_file)
pickle_file.close()
