# Team aslkjdf -- Anya Keller and Sebatian Cain
# IntroCS2 pd1
# HW45 -- Text Analysis, Webified
# 2015-05-11


novel = open('lit.txt','r')
file = open("wordtally.py", "w")

words = {} # dictionary for words

#sets up the novel to be read (lower case, removes punctuation)
novellist = ''
for letter in novel.read():
    if letter.isalpha() or letter == ' ' or letter == '-' or letter == '\n':
        novellist += letter
novellist = novellist.lower()
novellist = novellist.split()


#count 'em up! 
for word in novellist:
    if word in words:
        words[word] = words[word] + 1
    else:
        words[word] = 1

#string to stick into new file
newfile = "print '<table>'\n"
for thing in words:
    newfile += 'print "<tr><td>' + thing + '</td><td> ' + str(words[thing]) + '</td></tr>"\n'



#writing and stuff
    
file.write("#!/usr/bin/python \n\
# === LINE BELOW IS MAGIC TOO === \n\
print 'Content-Type: text/html\\n' \n\
 \n\
# === MORE MAGIC === \n\
print ' ' #Sha-Bang!!! \n\
print '<html>' \n\
print '<title> Word Count    </title>'   #thanks to Richard Lin's template \n\
print '<head> <h1> Word Count   </h1> </head>'    \n\
\n\
#WRITE CODESTUFF HERE \n\
\n\
")

file.write(newfile)
file.write("print '</table>' \n\
print '</html>' \
")

novel.close()
file.close()
