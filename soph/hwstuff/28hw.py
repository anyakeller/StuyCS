#Team Potato-Genkina -- Shamaul Dilmohamed, Anya Keller 
# IntroCS2 pd1
# HW28 -- Come Together
# 2015-04-15



'''
1. WvF: We have to go through all of the elements of the list no matter what, so it is best to use a for loop. 
2. WvF: We use a while loop because you are creating a list not interating through one
3. WvF: A for loop also works for iteratin through this list
'''

def  rmNegatives(L):
    n = []
    for thing in L:
        if thing >= 0:
            n.append(thing)

    return L

print str(rmNegatives( [5,4,3,2,1] )) , '[5,4,3,2,1]'
print str(rmNegatives( [5,-4,3,-2,1] )) , '[5,3,1]'


def listFib(n):
    x , y = 0 , 1
    l = [0]
    while n > 1:
        x, y = y , x + y
        l.append(x)
        n -= 1
        
    return l

print listFib(1) # [0]
print listFib(2) # [0,1]
print listFib(3) # [0,1,1]
print listFib(4) # [0,1,1,2] 


def sentify(L):
    s = ''
    for words in L:
        s += words + ' '
    return s

print sentify(['Star','trek','is','the','best!!!']) # Star trek is the best!!! 
print sentify([]) #
