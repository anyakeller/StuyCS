# Anya Keller
# IntroCS2 pd1
# HW32 -- Bucket List
# 2015-04-21

'''
def modeList(nums):
    l = []
    for num in nums:
        l += [0] * ((num + 1 )- len(l)) 
        l[num] += 1
       
    modes = []
    highest = max(l)
    pos = 0
    for num in l:
        if num == highest:
            modes.append(pos)
        pos += 1
    return modes
    
print modeList([3,3,4,200,200,5,5]) , [3,5,200]
print modeList([3,3,4,6,4,5,4]) , [4]

'''
#so apparently modeList only returns 1 number... M'kay
def modeList(nums):
    l = []
    for num in nums:
        l += [0] * ((num + 1 )- len(l)) 
        l[num] += 1
    
    return l.index(max(l))

print modeList([3,3,4,200,200,5,5]) , 3
print modeList([3,3,4,6,4,5,4]) , 4
print modeList([3,3,2000000,4,2000000,6,4,5,2000000,4,2000000]) , 2000000





def vBarGraphify(nums):
    pos = 0 #for location bars
    level = max(nums)
    s = ''
    while level > 0:
        while pos < len(nums):
            if nums[pos] >= level:
                s += '* '
            else:
                s += '  '
            pos += 1
        pos = 0
        print s
        s = ''
        level -= 1
    pos = 0
    while pos < len(nums):
        s += str(pos) + ' '
        pos += 1
    print s
    print '--' * (len(nums) -1) + '-'
    
    
vBarGraphify([2,4,1,0,5]) 
vBarGraphify([1,2,3,4,3,2,1])

    
    