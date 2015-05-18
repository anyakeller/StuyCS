'''
Team Monkeys - Mohammed Ullah, Anya Keller, Janice Bark
IntroCS2 pd 1
HW23 -- Anslatingtray Englishway intoway Igpay Atinlay
2015-03-30

 PIG LATIN RULES:
 1) If the first letter of the word is a vowel, then simply add way to the end of the word.
 2) If it's not a vowel, move the first letter back. Then check the second letter
 to see whether it is a consonant or not. If it is a consonant, then add it to the
 end of the word and repeat until you coem across a vowel. Then add ay.

OUTLINE:
A helper function will check the first letter of the word. It will return either True
(for vowel) or False(for consonant). This helper function will be called by the main function
, which will be recursive until it comes across the first vowel in the word.

DEVELOPMENT PLAN:
The simplest function we can write is to add way to the end of the word if it
begins with a vowel.
Next, we could add cases for if the first letter is not a vowel.
Finally, we could implement recursion for the words that contain more than one consonant
at the beginning.

Dev Log:
Janice stated what we should write
Mohammed typed
Anya tested cases
Everyone contributed to the information above.
'''

def isVowel(s):
    return s.lower() == 'a' or s.lower() == 'e' or s.lower() == 'i' or s.lower() == 'o' or s.lower() == 'u' or s.lower() == 'y'

def pig(s):
    if s[:2].lower() == 'qu':
        return s[2:] + 'quay'
    elif isVowel(s[0]):
        return s + 'way'
    elif isVowel(s[1]):
        return s[1:] + s[0].lower() + 'ay'
    else:
        return s[2:]+ s[0:2].lower() + 'ay'

print pig('piglatin')
#iglatinpay
print pig('chair')
#airchay
print pig('apple')
#appleway

#def letter(s):
#     return 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122

#just use s.isalpha()

'''
#old version

def translate(phrase):
    new = ''
    while phrase.find(' ') > 0:
        word = pig(phrase[:phrase.find(' ')])
        new += word + ' '
        phrase = phrase[phrase.find(' ') + 1:]
    new += pig(phrase)
    return new
        
print translate('I can speak piglatin')  
#Iway ancay eakspay iglatinpay
'''

def translate(phrase):
    count = 0
    word = 0
    new = ''
    while count < len(phrase):
        #print new , count, word  #debugging stuff
        if phrase[count].isalpha() == True:
            word += 1
        elif phrase[count].isalpha() == False:
            if word == 0:
                new += phrase[count]
            else:
                new += pig(phrase[count - word : count]) + phrase[count]
            word = 0
        count += 1
        if count == len(phrase) and phrase[count -1 ].isalpha() == True:
            new += pig (phrase[count - word:])
    return new

print translate('I can speak piglatin!!!')       
print translate('Are you a pineapple?')   
print translate('Sometimes I like to potate')   
print translate('I am the Queen of Shiba')   

        
    