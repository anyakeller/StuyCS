#!/usr/bin/python                                                               
# ====  LINE ABOVE IS MAGIC DO NOT MOVE =======                                 

# === LINE BELOW IS MAGIC TOO ===                                               
print 'Content-Type: text/html\n'

# === MORE MAGIC ===                                                            
print ' '

print '<html> <head><h1> Top 30 words in <i> The Time Machine </i> by H.G. Well\
s </h1><head>'

novel = open('lit.txt','r')
words = {} # dictionary for words                                          


#sets up the novel to be read (lower case, removes punctuation)                 
def setItUp():
    novellist = ''
    for letter in novel.read():
	if letter.isalpha() or letter == ' ' or letter == '-' or letter == '\n'\
:
            novellist += letter
    novellist = novellist.lower()
    novellist = novellist.split()
    return  novellist

#count 'em up!                                                                  
def countIt(x):
    words = {}
    for word in x:
        if word in words:
            words[word] = words[word] + 1
        else:
            words[word] = 1
    return words

def topValues(words):
    s={}
    largest,value = '',0
    for n in range(30):
        for x in words:
            if words[x] > value:
                largest = x
                value = words[x]
        s[largest] = words.pop(largest)
        largest , value = '',0
    return s

def makeTable():
    novellist = setItUp()
    words = countIt(novellist)
    topWords = topValues(words)
    print '<table>'
    for word in topWords:
        print '<tr><td>' + word + '</td><td>' + str(topWords[word]) + '</td></t\
r>'
    print '</table>'
    
    
#all the printy stuff happening                                                 
print '<p>'
makeTable()
print '</p><p>'
print "This eBook is for the use of anyone anywhere at no cost and with almost \
no restrictions whatsoever. You may copy it, give it away or re-use it under th\
e terms of the Project Gutenberg License included with this eBook or online at \
www.gutenberg.net"
print '</p>'
print '</html>'    
    
    
    