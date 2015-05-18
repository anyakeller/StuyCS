# Team __noun__ - Anya Keller and Andy Fernandez
# IntroCS2 pd1
# HW35 -- Put Your Plan Into Action
# 2015-04-25

'''
Plans:
1) Nouns, verbs, adj, etc. are lists
2) The function converts the string into a list
3) It then goes through the list and replaces the <> tagged words witha random word from the list
4) A helper function gets that random word and deletes it from this list
5) The list is joined as a string and it is returned 
'''

import random

#story
s =  'There once lived two siblings named <NAME> and <NAME>.  They liked to eat <PLNOUN> so much that one day, they ate too many and <VERB>.  Out of nowhere, a <NOUN> found them and granted them three wishes. Their first wish was to become masters of <NOUN>-riding.  Suddenly, they found themselves atop a <ADJ> <NOUN> flying across the galaxies.  Afeter a <ADJ> ride, they arrived in <PLACE>, where their steeds <VERB>.  For their second wish, they asked the genie to turn all the <PLNOUN> in the world into <ADJ> <PLNOUN>. As their final wish, they wished that they were back home in <PLACE>.  In the blink of an eye, they were back home, safe and <ADJ>.' 

#wordbank
noun = ['protractor','cabbage','fish','carbon','turkey','t-square','ball of mucus','sledgehammer']
plnoun = ['hamburgers','asteroids','big SAT words','wizards','peanuts','vertical bandsaws','1nt3r n3t tr011z']
verb = ['sweated','exploded','swam','sang','cried','defecated','imploded','re-took the SHSAT']
adverb = ['slowly','angrily','steadily','carfully','apathetically']
adj = ['purple','hella ugly','fishy','smelly','crabby','salty af','hungry']
name = ['Andy Fernandez','Anya Keller','Barack Obama', 'Leonardo DiCaprio', 'Icky Austraila','Cher','Michaelangelo', 'Henry VIII','King Arthur of the Round Table']
place = ["The United States of 'Murica",'The Bridge',"Mr. Moran's office",'Queens (AKA the suburbs)','Greece']

def word(x):   #chooses random word
    return x.pop(random.randrange(len(x)))
   
def fillBlanks(story):
    l = story.split()
    pos = 0
    for thing in l: #although I'm modifying the list, I'n not changing the length so for is okay to use
        if thing.count('<PLNOUN>') > 0:
            l[pos] = l[pos].replace('<PLNOUN>',word(plnoun))
        elif thing.count('<NOUN>') > 0:
            l[pos] = l[pos].replace('<NOUN>',word(noun))
        elif thing.count('<ADVERB>') > 0 :
            l[pos] = l[pos].replace('<ADVERB>',word(adverb))
        elif thing.count('<VERB>') > 0:
            l[pos] = l[pos].replace('<VERB>',word(verb))
        elif thing.count('<NAME>') > 0:
            l[pos] = l[pos].replace('<NAME>',word(name))
        elif thing.count('<PLACE>') > 0:
            l[pos] = l[pos].replace('<PLACE>',word(place))
        elif thing.count('<ADJ>') > 0:
            l[pos] = l[pos].replace('<ADJ>',word(adj))
        pos += 1
    s = ' '.join(l)
    return s
    
print fillBlanks(s)