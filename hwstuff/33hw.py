# Anya Keller
# IntroCS2 pd1
# HW33 -- Oh, Give Me a Home Where the Buffalo Roam
# 2015-04-22

'''
For merge I'm gonna use the bucket list strategy and fill the buckets.
Then, I'll empty the buckets into a new list
'''
#merges two lists and orders it (ascending)
def merge(L1,L2): 
    bucket = [] #this is a bucket
    for num in L1:    #for L1
        bucket += [0] * ((num + 1 )- len(bucket))  #makes bucket the right length
        bucket[num] += 1           #puts stuff in bucket
    for num in L2:    #for L2
        bucket += [0] * ((num + 1 )- len(bucket))  #makes bucket the right length
        bucket[num] += 1           #puts stuff in bucket
    pos = 0 #cuz .index() won't always work...
    l=[] #new list for dumping bucket
    for num in bucket:
        l += [pos] * num #putting stuff in the new list
        pos += 1
    return l

a = [0, 2, 4, 6, 8]
b = [1, 3, 5, 7]
merge(a,b) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print merge([5,4,3,16,8,9,3],[3,9,9,8,5,2,4]) #[2, 3, 3, 3, 4, 4, 5, 5, 8, 8, 9, 9, 9, 16]
print merge([],[]) # []
#print merge([20000000,213,234,76,3,5,5234],[1234,456546,1234,345]) #[3, 5, 76, 213, 234, 345, 1234, 1234, 5234, 456546, 20000000]  It works but it takes a few seconds

print '======NEXT==FUNCTION=============='

'''
There's a list and I'll put stuff in with a for loop and random.
Also the range is the same length as the list
'''
import random
#list len n of random numbers from 0 to (n - 1)
def randList(n):
    l = []  
    for num in range(n):
        l +=[random.randrange(n)] #generates random number in the range
    return l

print randList(5)  #Some list of len 5 with numbers from 0 to 4 inclusive
print randList(50) #same idea here
print randList(3)  #potato

print '======NEXT==FUNCTION=============='

'''
So ther are 5 numbers each in the range 0 to 255.
So I generate a random number 5 times in that range...
'''
#generates Ipv.4
def randIPv4():
    ip = ''
    for n in range(4):
        ip += str(random.randrange(256)) + '.' #ip gets numbersyay
    return ip[:-1] #get rid of last period

print randIPv4() #something like 99.123.248.207

print '======NEXT==FUNCTION=============='

#because the two lists are sorted
def meh(L1,L2):
    pos = 0
    for num in L2:
        while num < L1[pos]:
            pos += 1
        L1[pos-1] = L1[pos-1] + [num]
    return L1

a = [0, 2, 4, 6, 8]
b = [1, 3, 5, 7]
print merge(a,b) #[0, 1, 2, 3, 4, 5, 6, 7, 8]
print merge([5,4,3,16,8,9,3],[3,9,9,8,5,2,4]) #[2, 3, 3, 3, 4, 4, 5, 5, 8, 8, 9, 9, 9, 16]
print merge([],[]) # []
        
        
        
    

