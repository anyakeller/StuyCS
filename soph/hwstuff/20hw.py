# Anya Kelller
# IntroCS2 pd1
# HW20 -- Reaching Out to the Neighbors
# 2015-03-24

def closerNum(target,num1,num2):
    if abs(num1 - target) < abs(num2 - target):
        print str(target) + ' is closer to ' + str(num1)
    elif abs(num1 - target) > abs(num2 - target):
        print str(target) + ' is closer to ' + str(num2)
    else:
        print str(target) + ' is equidistant  to the numbers'

        
        
closerNum(8,20,10) # '8 is closer to 10'
closerNum(8,20,2) # '8 is closer to 2'
closerNum(8,-2,30) # '8 is closer to -2'
closerNum(8,10,6) # '8 is equidistant to the numbers'
