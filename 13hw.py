# Anya Keller
# IntroCS2 pd1
# HW13 -- The Handoff
# 2015-03-11
import math

def numRealRoots(a,b,c):
    z = b ** 2. - 4. * a * c
    if z > 0 :
        return 2
    elif z == 0:
        return 1
    elif z < 0:
        return 0
    else:
        return "You did something wrong; my code is just fine thankyouverymuch..."

def quadSolver(a,b,c):
    x = numRealRoots(a,b,c)
    z = (b ** 2.) - (4. * a * c)
    if x == 2:
        z =  math.sqrt((b ** 2.) - (4. * a * c))
        print (4 * a * c)
        print (b ** 2)
        print (-b + z)/(2. * a) , (-b - z)/(2. * a)
    elif x == 1:
        print -b/(2 * a) 
    elif x == 0:
        print 'no real roots'
    else: 
        print 'what did you do...?'

print numRealRoots(1,2,3) #--> 0
print numRealRoots(1,-6,9) #--> 1
print numRealRoots(1,3,2) #--> 2

print quadSolver(1,2,3) #--> 'no real roots'
print quadSolver(1,4,4) #--> -2
print quadSolver(1,-2,-15) #--> 5 -3 



    