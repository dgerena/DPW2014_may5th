Damasio Eli Gerena's Notes for quiz

#singe line comments!
'''Multi-line
name    Damasio Eli Gerena IV
date    may 5th 2014
class   dpw 2014 may
'''
#print "hello world!"

#variables
first_name='eli '
last_name='de man'
year_born=2014-1987
#year_born+= 1 # -= *= += /+ for assignment tonight!!!! mathmatic  assignment  operators !!!!!!!! must have a defined variable before use
#print year_born

#conditionals
'''
if year_born > 1995:
    print "you're a part of millenial generation"
elif year_born > 1978:
    print "you're a part of generation y"
elif year_born > 1965:
    print "you're a part of generation x"
else:
    print "these generations do not apply"
'''
#arrays
students=["eli","e7li","e6li","el4i","eli3","eli2",]
students.append("arturo")
students[0].split()

#dictionaries -associative arrays
#name_of_dict={'key':value}
class_info={"students": students,'roster count': 9,"room":"fs4a107"}

#loops
# for each loop
for s in students:
    pass
#for loop with a count
# for i in range (start, end ,inc/dec)
for i in range(0,10):
    pass
# also with random numbers
import random

#for loop with a count
# for i in range (start, end ,inc/dec)
for i in range(0,10):
    #print random.randrange(1,20)
    pass

#def
def calc_area(h,w):

    area=h*w
    print area

calc_area(300,200)

#format string method
user_name="guts"
message='''
Welcome home {user_name}!
'''

message=message.format(**locals())
#print message

#getting information from the user
first_name=raw_input('number:')
print str(int(first_name)+2)+",is tiring."
