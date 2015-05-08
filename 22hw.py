# Team Stuypulse-- Anya Keller, and everyone else on the robotics team
# IntroCS2 pd1
# HW22 -- Further Explorations in Toy_Encryption
# 2015-03-26

#how I did the challenge
#I used while loops and stuff to print all the possible shifts and I modifyied rot13Ch to accept a new parameter- shift



#from previous hw
def rotShiftChr(ch, shift): #character, shift
    value = ord(ch)
    if 65 <= value <= 90:  #upper case sturfff
        value +=shift
        if value > 90:
            value = 65 + (value - 91)
    elif 97 <= value <= 122:    #upper case
        value +=shift
        if value > 122:
            value = 97 + (value - 123)
    else:
        return ch   #punctuation stuff
    return chr(value)


#heh i did this already
def rot13Wrd(word):
    new = ''
    count = 0
    while count < len(word):
        if word[count] == ' ':
            new += ' '
        else:
            new += rotShiftChr(word[count],13)
        count += 1
    return new

print rot13Wrd('JABBERWOCKY') # 'WNOOREJBPXL'
print rot13Wrd('My code is TERRIBLE!!!') # 'Zl pbqr vf GREEVOYR!!!'


#CHALLENGE  DUN DUN DUNNNNNNNN

def rotIDK():
    #setup
    shift = 0
    possible = ''
    word = raw_input('plz give meh en encrypted phrase: ')  #so cool
    print 'the original word is ' + str(word)
    
    #here we go!
    while shift < 26:
        count = 0
        new = ''
        while count < len(word):
            if word[count] == ' ':
                new += ' '
            else:
                new += rotShiftChr(word[count], shift)
            count += 1
        possible += 'shift ' + str(shift) + ', new word is ' + new + '\n'
        shift += 1
    possibleList = possible.split('\n')
    print 'All the possibilities'
    print possible
    print '\n which shift made the most sence?'
    correctShift = raw_input('please answer a numer: ') #derp
    print ' \n Here you go! ' + possibleList[int(correctShift)]

rotIDK()
#plz give meh en encrypted phrase: #deoh
#the original word is deoh
#shift 0, new word is deoh
#.... 
#which shift made the most sence?
#please answer a numer: #23
#shift 23, new word is able




#rotIDK('Roi roi! Ry ry! Cyzr-Pbycr CSXQ! tecd cdyvo dro cryg!')
#I found it
#shift 16, new word is Hey hey! Ho ho! Soph-Frosh SING! just stole the show!

