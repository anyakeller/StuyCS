# Anya Keller
# IntroCS2 pd1
# HW12 -- Letters & Numbers
# 2015-03-11

def gradeConv(g):
    if g > 100:
        return 'ayyy'
    elif g >= 90:
        return 'A'
    elif g >= 80:
        return 'B'
    elif g >= 70:
        return 'C'
    elif g >= 65:
        return 'D'
    elif g >= 0:
        return 'F'
    else :
        #raise ValueError("You broke the system")
        return 'Can you count?!?!?'

#test cases
print gradeConv(105)
#expecting 'ayyy'
print gradeConv(98)
#expecting 'A'
print gradeConv(87)
#expecting 'B'
print gradeConv(75)
#expecting 'C'
print gradeConv(66)
#expecting 'D'
print gradeConv(56)
#expecting 'F'
print gradeConv(-4)
#expecting 'Can you count?!?!?'
print gradeConv('hi')



def passJudgement(letterGrade):
    if letterGrade == "A":
        print "You might be able to get into college!"
    elif letterGrade == "B":
        print "Try harder next time"
    elif letterGrade == "C":
        print "You fail"
    elif letterGrade == "D":
        print "Beyond failing"
    elif letterGrade == "F":
        print "You're screwed"
    elif letterGrade == "ayyy":
        print "Congrats, you might be smarter than a monkey"
    elif letterGrade == "Can you count?!?!?":
        print "I can, can you?"
    else: 
        print gradeConv(letterGrade)

print passJudgement('A')
#expecting "You might be able to get into college!"
print passJudgement('B')
#expecting "Try harder next time"
print passJudgement('C')
#expecting "You fail"
print passJudgement('D')
#expecting "Beyond failing"
print passJudgement('F')
#expecting "You're screwed"
print passJudgement('ayyy')
#expecting "Congrats, you might be smarter than a monkey"
print passJudgement(92)
#expecting 'A'
