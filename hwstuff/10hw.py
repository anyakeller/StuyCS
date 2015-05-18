# Anya Keller
# IntroCS2 pd1
# HW10 -- Boolean Logic, Conditionals, Oh My!
# 2015-03-05


import math

def cartDist(X1,Y1,X2,Y2):
    return math.sqrt( (X2 - X1) ** 2 + (Y2- Y1) ** 2)

print cartDist(0,0,0,0)
#expecting 0
print cartDist(4,4,4,4)
#expecting 0
print cartDist(0,0,3,4)
#expecting 5

def pythTriple(a,b,c): 
    if a == 0 or b == 0 or c == 0:
        return False
    else:
        return (a ** 2 + b ** 2) == (c ** 2)

print pythTriple(0,0,0) 
#expecting false
print pythTriple(3,4,5) 
#expecting true
print pythTriple(3,4,6) 
#expecting False
print pythTriple(32,255,257)
#expecting True

