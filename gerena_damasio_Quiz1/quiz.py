'''
Damasio Eli Gerena IV
Basic Python Syntax Quiz
May 7 2014
'''
def calc_area(h,w):#calculating the area
    if h == w :
        print "The area of your square is " + str(h * w)
    else:
        print "The area of your rectangle is " + str(h *w)#math good yup its good

calc_area(int(raw_input("Height:")),int(raw_input("Width:")))#area calced out real pretty

def count_down(bottles):
    for i in range(bottles,0,-1):
        print str( i ) + " Bottles of Beer on the Wall, "
        print str( i ) + " Bottles of Beer... take one down pass it around "
        print str( i - 1) + " Bottles of Beer on the Wall!"

count_down(int(raw_input("Bottles of Beer:")))