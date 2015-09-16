# Team MA - Anya Keller and Mohammed Ullah
# IntroCS2 pd1
# HW31 -- Stats on Stats on Stats
# 2015-04-20

def modeListA(nums):
    prevn= nums[0]
    xtimes = nums.count(prevn)
    for n in nums:
        if nums.count(n) > xtimes:
            prevn = n
    return prevn , nums.count(prevn)

print modeListA([2,3,6,8,6])     #(6 , 2)
print modeListA([7,7,7,6,8,6])   #(7 , 3)
print modeListA([2,7,7,6,8,6])   #(6 , 2)
print modeListA([2,6,6])         #(6,  2)

print '==========='

def modeListB(nums):
    modes = []
    x , times = modeListA(nums)[0] , modeListA(nums)[1]
    while modeListA(nums)[1] >= times:
        x = modeListA(nums)[0]
        modes.append(x)
        count = times
        while count > 0:
            nums.remove(x)
            count -= 1
    return modes
    
print modeListB([2,3,6,8,6,7,7])   #[7,6]
print modeListB([7,7,7,6,8,6])     #[7]
print modeListB([7,7,8,6,8,6,2])   #[7,8,6]

print '==========='

def vBarGraphify(nums):
    top = max(nums)
    s = ''
    while top > 0:
        for data in nums:
            if data >= top:
                s += '* '
            else:
                s += '  '
        print s
        s = ''
        top -= 1
    pos = 0
    while pos < len(nums):
        s += str(pos) + ' '
        pos += 1
    print s
    print '--' * (len(nums) -1) + '-'

import timeit

start = timeit.default_timer()    
    
vBarGraphify([2,4,1,0,5]) #yay it works!!!
vBarGraphify([1,2,3,4,3,2,1])

stop = timeit.default_timer()

print stop - start 
