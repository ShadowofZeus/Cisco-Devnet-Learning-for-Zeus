import nester
import pickle

man = []
other = []

try:
    data = open('yolo.txt',mode='rt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()        #the strip function removes all whitespace
            if role == 'Man':
                man.append(line_spoken)

            elif role == 'Other Man':
                other.append(line_spoken)

        except ValueError:
            pass
            data.close()

except IOError:
     print('The datafile is missing!')

try:                                                        #with statement in action here
    with open('man_data.txt', 'wb') as man_file:             #open man_data.txt and write to it, create file object called man_file
        pickle.dump(man, man_file)                           #write to file man_file from pickle dump function
    with open('other_data.txt', 'wb') as other_file:
        pickle.dump(other, other_file)
except IOError as err:                                      #create exception object i.e err
    print('File error: ' + str(err))                        #change the error output to string format so that it is printable onscreen

except pickle.PickleError as perr:
    print('Prickling Error:'+str(perr))

###########################################################
