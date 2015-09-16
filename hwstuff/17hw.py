# Anya Keller
# IntroCS2 pd1
# HW17 -- 000 000 111
# 2015-03-17

def bondify(name):
    nameList = name.split(' ')
    if len(nameList) > 2:
        print "Ha!  People don't have middle names!  Why woud you?"
    else:
        print 'The name is ' +  nameList[1] + ' , ' + name
    
bondify('Anya Keller')
#The name is Keller , Anya Keller

bondify('Anya Laskin Keller')
#Shhhhh! There is no such thing as middle names

#in case you wanted us to only use what we learned in class
def bondifyW(name):
    x = 1
    first = ''
    last = ''
    while name[x] != ' ':
        first += name[x]
        x += 1
    x += 1  
    while x <= len(name) - 2:
        last += name[x]
        x += 1
    last += name[x]
    print 'The name is ' + last + ' , ' + name
    
bondifyW('Anya Keller')
#The name is Keller , Anya Keller