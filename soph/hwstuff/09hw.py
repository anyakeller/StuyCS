# Anya Keller
# IntroCS2 1
# HW09 -- Visiting Old Friends
# 2015-03-04

import math

def areaCirc(r):
    return math.pi * r ** 2.

def areaWasher(radInner,radOuter):
    return areaCirc(radOuter) - areaCirc(radInner)

def sumOfSquares(a,b):
    return (a ** 2 ) + (b ** 2)



print areaCirc(4)
#should be 50.2654824574 

print areaWasher(3,5)
#should be 50.2654824574 

print sumOfSquares(4,5)
#should be 41