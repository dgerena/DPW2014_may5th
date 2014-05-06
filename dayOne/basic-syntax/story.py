'''
As "name" was going to "location" i met a "person" with "number"
"family pos1"'s the 'repeat number' "family pos1" had 'repeate number' "item1"'s the 'repeate number' "item1"'s
had 'repeate number' "animal1"'s the 'repeate number' "animal1"'s had 'repeate number' "animal2"'s. "animal2"'s,
"animal"'s, "item1"'s and "family pos1"'s how many were going to saint ives?

num of guess is 3, if they type reset it will find if its a 1st guess
or 2nd if its a 2nd add 1 if its a 1 mult by 3 and subtract 1 each guess.after 3rd guess if 0 += 3
'''


name=raw_input("Your name:")
location=raw_input("A location:")
person=raw_input("Gender:")
number=raw_input("Any number:")
fam_pos=raw_input("wife, girlfriend, or significant others title.:")
item=raw_input("A container:")
animal=raw_input("A animal:")
animal2=raw_input("Baby animal:")
my_array=[]
my_array.extend([name,location,person,number,fam_pos,item,animal,animal2])

guesses={"correct": 1,"Wrong": not 1}

def question(arr):
    q='''As {arr[0]} was going to {arr[1]} i met a {arr[2]} with {arr[3]}
    {arr[4]}\'s the {arr[3]} {arr[4]} had {arr[3]} {arr[5]}\'s the {arr[3]} {arr[5]}\'s
    had {arr[3]} {arr[6]}\'s the {arr[3]} {arr[6]}\'s had {arr[3]} {arr[7]}\'s. {arr[7]}\'s,
    {arr[6]}\'s, {arr[5]}\'s and {arr[4]}\'s how many were going to {arr[1]}?'''
    print q.format(**locals())

question(my_array)

def quesing(n):
    user_guess
    for i in range(0,2):
