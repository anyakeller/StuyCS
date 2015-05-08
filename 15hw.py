# Anya Keller
# IntroCS2 pd1
# HW15 -- Loopy
# 2015-03-16

import math

def sumDigits(n):
    x = 0
    while n > 0:
        x = x + (n % 10)
        n = n // 10
    return x

print sumDigits(123)
#6
print sumDigits(1234567)
#28

def squares (n):
    x=1
    integers=[]
    while x<=n:
        integers.append(x)
        x=x+1
    print integers , n*n

squares(5)
#[1, 2, 3, 4, 5] 25
squares(12)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 144


def sumPerfSqs(n):
    count = 1
    sums = 0
    while count <= n:
        if math.sqrt(count) % 1 == 0:
            sums = sums + count
        count += 1
    print sums
    
sumPerfSqs(10)
#14
sumPerfSqs(50)
#140
        