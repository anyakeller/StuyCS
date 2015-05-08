# Team Stay_FOR_a_WHILE -- Anya and Mo
# IntroCS2 pd1
# HW29 -- Removal Three Ways
# 2015-04-16

'''
POP: 
syntax: list.pop(obj=list[-1])
behavior: Removes and returns the last (or any) object in the list

REMOVE:
syntax: list.remove(obj)
behavior: removes obj from the list

DEL:
syntax: del L[i]
behavior: Unbinds a variable 

SWAGyolo prefers .remove for use in rmNegatives() because you are modifying the list by removing things.

'''


# THIS IS HOW WE DO IT UHNUHNUHNUHN
# (Basically I didn't use things that we didn't 'lean' yet)
def rmNegatives(L):
    pos = 0
    while pos < len(L):
        if L[pos] < 0:
            if pos == len(L) -1:
                L[0:] = L[:-1]
            else:
                x = L[pos+1:]
                L[0:] = L[:pos]
                L.extend(x)
        else:
            pos += 1

L = [1,2,3,4,-1]
rmNegatives(L)
print L , [1,2,3,4]

L = [1,2,-1,4,7]
rmNegatives(L)
print L , [1,2,4,7]

L = [-1,2, -2,3,4,-1]
rmNegatives(L)
print L , [2,3,4]

L = [-1,2, -2,-3,4,-1]
rmNegatives(L)
print L , [2,4]

print '==============================================='
# Okay here is the other stuff
def rmNegatives2(L):
    count = 0
    while count < len(L) :
        if L[count] < 0:
            L.remove(L[count])
        else:
            count += 1  #else because you don't want to skip elements

L = [1,2,3,4,-1]
rmNegatives2(L)
print L , [1,2,3,4]
    

L = [1,2,-1,4,7]
rmNegatives2(L)
print L , [1,2,4,7]

L = [-1,2, -2,3,4,-1]
rmNegatives2(L)
print L , [2,3,4]

L = [-1,2,-2,-3,4,-1]
rmNegatives2(L)
print L , [2,4]


