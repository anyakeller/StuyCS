# Anya Keller
# IntroCS2 pd1
# HW12 -- Repetition, Two Ways
# 2015-03-13

def factR(n):
    if n > 1:
        return n * factR(n-1)
    elif n == 1 or n == 0:
        return 1
    elif n < 0 :
        return "No negative numbers!!!"
    else:
        return "Was that a number?"
    
print factR(0) #1
print factR(1) #1
print factR(2) #2
print factR(4) #24


#I'll clean up the code if I have time because I have robotics sat and sunday
def factW(n):
    y = n * (n - 1)
    n = n - 2
    while n > 1:
        y = y * n
        n = n - 1
    if n == -2 or n == -1:
        y = 1
    return y

print factW(0) #1
print factW(1) #1
print factW(2) #2
print factW(4) #24