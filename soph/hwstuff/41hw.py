# Anya Keller                                                                   
# IntroCS2 pd1                                                                  
# HW41 -- Clever Problem Solving                                                
# 2015-05-05                                                                    

## PROBLEM 1 -- Multiples of 3 and 5                                            
## algorithm:                                                                   
##   start counter                                                              
##   while loop                                                                 
##   check if multiple --> add to tot                                           
##   return tot                                                                 

def listmult():
    x = 0
    tot = 0
    while x < 1000:
        if x % 3 == 0 or x % 5 == 0:
            tot += x
        x += 1
    return tot
print listmult()  # 233168                                                      

## PROBLEM 2 -- Even fib                                                        
## algorithm:                                                                   
##    generates fib                                                             
##    if even addes to a counter 'tot'                                          

def evenFib():
    prev , fib = 0 , 1
    tot = 0
    while fib < 4000000:
        prev , fib = fib , prev + fib
        if fib % 2 == 0:
            tot += fib
    return tot

print evenFib() #4613732                                                        


## PROBLEM 4 -- Palendrome                                                      
## algorithm:                                                                   
##   converts product to a string                                               
##   finds the halfway point in the string                                      
##   compares first and last half of string                                     
##   if equal, exit loop  

def palind():
    x , y = 100, 100
    times = x * y
    strtime , half = str(times), len(str(times))/2
    while strtime[:half] != strtime[::-1][:half] and y < 999:
        while strtime[:half] != strtime[::-1][:half] and x < 999:
            times = x * y
            strtime , half = str(times), len(str(times))/2
            x+=1
        x = 100
	y += 1
    return times
print palind() #10201  


## PROBLEM 5 -- Smallest mult
## algorithm:
##    helper checks if it is evenly divisible by numbers 1 - 20
##    current number 'x'
##    while helper of the current number is False, continue to run but with one higher number
##    when it returns True, return the current number 

def help5(x):
    n = 2
    while n <= 20:
        if x % n != 0:
            return False
        n += 1
    return True

def smallestmul():
    x = 1
    while help5(x) == False:
        x += 1
    return x

print smallestmul()  #232792560

