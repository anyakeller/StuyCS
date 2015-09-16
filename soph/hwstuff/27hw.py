
# Anya Keller
# IntroCS2 pd1
# HW27 -- Back in the [Co]Driver's Seat, Looping_FTW
# 2015-04-14

def listSum(L):
    x = 0
    for thing in L:
        x += thing
    return x

print listSum( [0,1,2,3] ) , 6
print listSum( [] ) , 0
print listSum( [5] ) , 5

def minVal(L):
    if len(L) == 0:
        return 'empty list'
    x = L[0]
    L =L[1:]
    for thing in L:
        if x > thing:
            x = thing
    return x

print minVal( [3] ) , 3
print minVal( [5,4,3,2,1] ) , 1
print minVal( [] ) , 'empty list'

def listFind(L,q):
    count = 0
    if len(L) == 0:
        return  'bad input'
    for thing in L:
        if thing == q:
            return count
        count += 1
    return -1

print listFind([5,4,3,2,1], 2) , 3
print listFind([5,4,3,2,1], 6) , -1
print listFind([5,4,'cat','dog','cat'], 'cat') , 2
print listFind([], 'cat') , 'bad input'

def minPos(L):
    count = 0
    pos = 0
    if len(L) == 0:
        return 'empty list'
    x = L[0]
    L =L[1:]
    for thing in L:
        count += 1
        if x > thing:
            x = thing
            pos = count
    return pos
print minPos( [3] ) , 0
print minPos( [5,4,1,2,8] ) , 2
print minPos( [5,4,3,2,1] ) , 4

