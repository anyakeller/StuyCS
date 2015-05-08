# Team ThermodynamicsMakesMeCri -- Anya Keller and Edward Tsang
# IntroCS2 pd1
# HW43 -- What's the FrequencyPlan, Kenneth?
# 2015-05-07


novel = open('novel.txt','r')
file = open("wordoc.txt", "w")

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

#writes to a new file
newfile = 'Word Occourences\n\n'
for thing in words:
    newfile += '- ' + thing + ': ' + str(words[thing]) + '\n'


file.write(newfile)

novel.close()
file.close()


'''
SWAGYOLO
THE s.strip([char]) 
meathod gets rid of the [char] appearances in string s!!!
SUUUUUGOIII 
'''