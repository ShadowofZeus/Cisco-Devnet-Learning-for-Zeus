
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data=f.readline()
        return(data.strip().split(','))

    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

"""
this code is all about sanitizing string data to a uniform format
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

james=get_coach_data('james.txt')
julie=get_coach_data('julie.txt')
mikey=get_coach_data('mikey.txt')
sarah=get_coach_data('sarah2.txt')

""""
james=sorted([sanitize(t) for t in james])                 #list comprehension in action for transforming list data
julie=sorted([sanitize(t) for t in julie])                  #function does better job than this
mikey=sorted([sanitize(t) for t in mikey])
sarah=sorted([sanitize(t) for t in sarah])
"""

unique_james = []
for each_t in james:
    if each_t not in unique_james:
        unique_james.append(each_t)
#print(unique_james[0:3])

unique_julie = []
for each_t in julie:
    if each_t not in unique_julie:
        unique_julie.append(each_t)
#print(unique_julie[0:3])

unique_mikey = []
for each_t in mikey:
    if each_t not in unique_mikey:
        unique_mikey.append(each_t)
#print(unique_mikey[0:3])

unique_sarah = []
for each_t in sarah:
    if each_t not in unique_sarah:
        unique_sarah.append(each_t)
#print(unique_sarah[0:3])



sarah_data={}
sarah_data['Name']=sarah.pop(0)
sarah_data['DOB']=sarah.pop(0)
sarah_data['Times']=sarah
print(sarah_data['Name'] + "'s fastest times are: " +
str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
