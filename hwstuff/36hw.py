# Team __noun__ - Anya Keller and Andy Fernandez
# IntroCS2 pd1
# HW36 -- Tune Your Engine
# 2015-04-27

'''
Plans:
1) Nouns, verbs, adj, etc. are lists
2) The function converts the string into a list
3) The identifier '<SOMETHING>' is set to tag and the list becomes the rest of the list
4) It then goes through the list and replaces the <> tagged words witha random word from the list
5) A helper function gets that random word and deletes it from this list
6) The list is joined as a string and it is returned 

New features in v2:
1) SimpleTense verbs
2) Past
3) Future
'''

import random

#story
s =  'There once lived two siblings named <NAME> and <NAME>. They had <PASTPART> <PLNOUN> but became <ADJ>. Their <NOUN> wanted to <VERBFUTURE> <PLNOUN> with <NAME>. However, it remembered that <NAME> once <VERBPAST> all the way to <PLACE>. They liked to eat <PLNOUN> so much that one day, they ate too many and <VERBPAST>.  Out of nowhere, a <NOUN> found them and granted them three wishes. Their first wish was to become masters of <NOUN>-riding.  Suddenly, they found themselves atop a <ADJ> <NOUN> flying across the galaxies.  After a <ADJ> ride, they arrived in <PLACE>, where their steeds <VERBPAST>.  For their second wish, they asked the genie to turn all the <PLNOUN> in the world into <ADJ> <PLNOUN>. As their final wish, they wished that they were back home in <PLACE>.  In the blink of an eye, they were back home, safe and <ADJ>.' 

#wordbank
noun = ['<NOUN>','protractor','cabbage','fish','carbon','turkey','t-square','ball of mucus','sledgehammer']
plnoun = ['<PLNOUN>','hamburgers','asteroids','big SAT words','wizards','peanuts','vertical bandsaws','1nt3r n3t tr011z']
verbSimple = ['<VERBSIMPLE>','drinks','drives','sings','steals','writes','makes']
verbPast = ['<VERBPAST>','sweated','exploded','swam','sang','cried','defecated','imploded','re-took the SHSAT','drank','drove','sang','stole','wrote','made']
verbFuture = ['<VERBFUTURE>','drink','drive','sing','steal','write','make']
pastParticiple = ['<PASTPART>','drunk','driven','sung','stolen','written','made']
preposition = ['<PREPOSITION>','at','on','after','before']
conjunction = ['<CONJUNCTION>','but','when','and']
adverb = ['<ADVERB>','slowly','angrily','steadily','carfully','apathetically']
adj = ['<ADJ>','purple','hella ugly','fishy','smelly','crabby','salty af','hungry']
name = ['<NAME>','Andy Fernandez','Anya Keller','Barack Obama', 'Leonardo DiCaprio', 'Icky Austraila','Cher','Michaelangelo', 'Henry VIII','King Arthur of the Round Table']
place = ['<PLACE>',"The United States of 'Murica",'The Bridge',"Mr. Moran's office",'Queens (AKA the suburbs)','Greece']
tags = [plnoun,noun,adverb,verbSimple,verbPast,verbFuture,pastParticiple,preposition,name,place,adj,conjunction]

def word(x):   #chooses random word
    return x.pop(random.randrange(len(x)))

def madlibify(story):
    l = story.split()
    for taglist in tags:
        #sets tags
        tag = taglist[0]
        taglist = taglist[1:]
        #begin iteration
        pos = 0
        while pos < len(l):
            if tag in l[pos]:
                l[pos] = l[pos].replace(tag,word(taglist))
            pos += 1
    s = ' '.join(l)
    return s
    
print madlibify(s)
