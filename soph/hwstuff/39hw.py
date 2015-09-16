# Anya Keller                                          
# IntroCS2 pd1  
# HW39 -- ASCIIng About Your Visage     
# 2015-04-30   


def common(L1,L2):
    l = []
    for el in L1:
        if el in L2:
            l += [el]
    return l

print common( [1,5,4,3,2] , [4,5,10,15] ) # [4,5]
print common([2,3,1,4,5],[7,2,1,6]) # [2,1]

'''
For alphabetize, I'll use nested loops and a list for the sorted names.
Outer loop --> goes though all the names
inner loop --> places them in l
if/elif/else statements --> cover all the cases and handle letters

'''

def alphabetize(names):
    hi = names.split(',')
    names = []
    joinCount = len(hi) 
    while joinCount > 0:
        names = names + [hi[joinCount - 2] + ' ' + hi[joinCount-1]]
        joinCount -= 2

    l = [] # sorted names go here
    for name in  names :
        lPos= 0 #name in l
        letterPos = 0 #for iterating though names
        while lPos <= len(l):
            if len(l) == 0:
                l += [name + '\n']
                lPos = len(l) +1
            elif lPos == len(l) or letterPos == len(name):
                l += [name]
                lPos = len(l) +1
            elif ord(name[letterPos]) < ord(l[lPos][letterPos]) or letterPos == len(l[lPos]):
                l = [name + '\n'] + l
                lPos = len(l) +1
            elif ord(name[letterPos]) == ord(l[lPos][letterPos]):
                letterPos += 1
            else:
                lPos += 2
        letterPos = 0
        lPos = 0
        names = ''.join(l)
    return names

print alphabetize( 'Wayne,Bruce,Kent,Clark,Parker,Peter' ) # Kent Clark\nParker Peter\nWayne Bruce
print 
print alphabetize( 'Keller,Anya,Keller,Hellen,Keller,Williams(real estate),Laskin,Rebekah' )  # Keller Anya\nKeller Hellen\nKeller Williams(real estate)\nLaskin Rebekah

                
            