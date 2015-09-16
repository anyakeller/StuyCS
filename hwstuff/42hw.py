# Team ThermodynamicsMakesMeCri -- Anya Keller and Edward Tsang                 
# IntroCS2 pd1                                                                  
# HW42 -- Four de Toid Thyme                                                    
# 2015-05-06                                                                    

def translate(word):
    dictionary = {'ni hao':'hello','swagyolo':"I think I'm cool",'hou':'monkey'\
,'yi':'one','hao hao':'edward','hao':'good','ma':'horse, mom, <question>'}
    if word in dictionary:
        return dictionary[word]
    else:
        return None

print translate('ni hao')
print translate('ma')

def modeLB(nums):
    dictionary={}
    for w in nums:
        if w in dictionary:
            dictionary[w] = dictionary[w] + 1
        else:
            dictionary[w] = 1
    return dictionary.keys()[dictionary.values().index(max(dictionary.values()))]

print modeLB([3,5,2,3]) #3
print modeLB([3,5,2,7,7])  #7