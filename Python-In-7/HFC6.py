"""
#Learning to define and use a Class  //Inheriting List class instead of writing class from scratch
class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

"""
def sanitize(time_string):
    if '-' in time_string:
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return(time_string)
    (mins,secs)=time_string.split(splitter)

    return(mins + '.' + secs)


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list._init_([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set([sanitize(t) for t in self]))[0:3])


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return(AthleteList(templ.pop(0), templ.pop(0), templ))

    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

"""                                 #Not needed anymore as List class has been inherited.
def add_time(self,time_value):
    self.times.append(time_value)

def add_times(self,list_of_times):
    self.times.extend(list_of_times)
"""
james=get_coach_data('james2.txt')
julie=get_coach_data('julie')
mikey=get_coach_data('mikey2')
sarah=get_coach_data('sarah2')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))