# Anya Kelller
# IntroCS2 pd1
# HW18 -- 000 000 111, v10 and more
# 2015-03-20

def bondify(name):
    split = name.split(' ')
    print 'The name is ' + split[1] + ' , '+ name

bondify ('Anya Keller')
#The name is Keller , Anya Keller


def replace(s,q,r):
    sl = len(s)
    ql = len(q)
    rl = len(r)
    while s.find(q) >= 0:
        s = s[0:s.find(q)] + r + s[s.find(q)+ql:]
    print s
    
replace('Winter is coming', 'Winter', 'Spring')
#Spring is coming

replace('OMG I DID IT YEY', 'DID IT', 'I AM A FREAKING POTATO')
#OMG I I AM A FREAKING POTATO YEY

replace('hi I am such swagyolo that I am a potato SwagI','I', ' nope ')
#hi  nope  am such swagyolo that  nope  am a potato Swag nope 
