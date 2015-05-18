# Team Stuypulse-- Anya Keller, and everyone else on the robotics team
# IntroCS2 pd1
# HW21 -- Cereal-Grade Encryption
# 2015-03-25

def rot13Chr(ch):
    value = ord(ch)
    if value <= 90:
        value +=13
        if value > 90:
            value = 65 + (value - 91)
    elif value <= 122:
        value +=13
        if value > 122:
            value = 97 + (value - 123)
    else:
        return "whatttttttt"
    return chr(value)

print rot13Chr('a') #n
print rot13Chr('A') #N
print rot13Chr('y') #m
print rot13Chr('Y') #M

def printEmAll():  #no
    upper = 65  #to 90
    lower = 97 #to 122
    
    while upper <= 90:
        print chr(upper) + '<->' + rot13Chr(chr(upper))
        upper += 1
    while lower <= 122:
        print chr(lower) + '<->' + rot13Chr(chr(lower))
        lower += 1
        
printEmAll()

def rot13Wrd(word):
    new = ''
    count = 0
    while count < len(word):
        if word[count] == ' ':
            new += ' '
        else:
            new += rot13Chr(word[count])
        count += 1
    return new

print rot13Wrd('JABBERWOCKY') # 'WNOOREJBPXL'
print rot13Wrd('My code is TERRIBLE') # 'Zl pbqr vf GREEVOYR'