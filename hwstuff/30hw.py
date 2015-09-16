# Anya Keller
# IntroCS2 pd1
# HW30 -- Stat-tastic
# 2015-04-17

def meanList(nums):
    if len(nums) == 0:
        return 'empty list'
    return (1.0 * sum(nums)) / len(nums)

print meanList([1,4,5,6]) , 4.0
print meanList([3,5,6,7,8,7,11,5,6,3,2]),  5.72727272727
print meanList([]) , 'empty list'

print '------------------------------------------'

def medList(nums):
    nums.sort()
    if len(nums) % 2 != 0:
        return nums[(len(nums) / 2)]
    else:
        return (nums[(len(nums) / 2)-1] + nums[(len(nums)/2)]) / 2.0

print medList([1]) ,1
print medList([2,3]) ,2.5
print medList([12,4,6,8]) ,7
print medList([2,4,12,5,7]) , 5

print '------------------------------------------'

def barGraphiphy(nums):
    for thing in nums:
        print str(nums.index(thing)) + ':' + thing*'='

barGraphiphy([2,4,6])
'''
0:==
1:====
2:======
'''

barGraphiphy([3,7,1,55,0,6,3])
'''
0:===
1:=======
2:=
3:=======================================================
4:
5:======
'''
