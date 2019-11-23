import pickle

pickle_file = open("emp1.dat",'rb')
name_list = pickle.load(pickle_file)
skill_list =pickle.load(pickle_file)
print(name_list ,"and", skill_list)
