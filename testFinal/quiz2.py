#!/usr/bin/python
print 'Content-Type: text/html\n'
print ' ' #Sha-Bang!!!
#here we go!!! 

import cgi
import cgitb
cgitb.enable()

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
form = cgi.FieldStorage()

def remove(user):
    infile = open('loggedin.txt','r')
    text = infile.read()
    infile.close()
    html = ''
    if (user+",") in text:
        #remove code
        html += "<p style = 'font-size:20 color:#A00000'>Hello<br>" + user + "! </p>"
        return html

if 'user' in form:
    user = form['user'].value
if 'magicnumber' in form:
    magicNumber = form['magicnumber'].value

def securefields():
    if 'user' in form and 'magicnumber' in form:
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        return "?user="+user+"&magicnumber="+magicnumber
    else:
        return ""
if 'user' in form:
    user = form['user'].value
else:
    user = ""
if 'magicnumber' in form:
    magicNumber = form['magicnumber'].value
else:
    magicNumber = ""
def header():
    header = ''' 
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <script src="quiz.js"></script>
        <title>Quiz Results</title>
    </head>
<body>

<div id="menu"> 
    <span id="top">Are you prepared?</span> 
<li id="nav"><a href="home.py''' + securefields() + '''">Home</a></li>
<li id="nav"><a href="tools.py''' + securefields() + '''">Equipment</a></li>
<li id="nav"><a class = "active" href="quiz.py''' + securefields() + '''">Quiz</a></li>
<li id="nav"><a href="safehouses.py''' + securefields() + '''">Safehouses</a></li>
<br>
<span id="top">Account info</span>
<li id="nav">'''
    if 'user' in form:
        header += "<center>" + remove(user) + "</center>"
        header += '''<a href="logout.py''' + securefields() + '''">Logout</a><br></div>'''

    else:
        header += '''
            <li id="nav">
                <a href = "login.html">Login</a>
            </li>
            <li id = "nav">
                <a href = "register.html">Register</a>
            </li> '''
    header += ''' </div>
<div id="right">

<center><span id="name">The Zombie Survivor's Handbook</span></center>
<h2>Quiz Results</h2>
'''
    return header
print header()
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        if type(formData[k]) == list:
            d[k] = []
            for el in formData[k]:
                d[k] += [el]
        else:
            d[k] = formData[k].value
    return d
d = FStoD()
#print d

questions = {'q1':['How does the disease spread?','water','air','contact','all of the above'], \
    'q2':['How can I tell if I have it? ','You begin to want brains','You already do.  Everyone has it.','You show signs of internal bleeding','Headaches and stuff'], \
    'q3':['How do you kill a zombie?','carefully','Destroy their brain','Shoot them in the heart','decapitate them'], \
    'q4':['Do zombies need to breathe?','they are human so they need oxygen like all of us','they can hold their breath longer but they still need air','they are technically dead so breathing is not needed','since they are falling apart, they need to breathe even more than we do'],\
    'q5':['Is there a known cure?','There is no known cure.','The only cure is being kept secret by the govenment','The CDC is currently distributing the cure','Scientists found a cure but it is too difficult to mass produce'], \
    'q6':[ 'Which of these would be best to kill a zombie that is right next to you?','rifle','pistol','machine gun','knife'], \
    'q7':[ "There are two zombies coming towards you, only inches away, and you're backed into a corner. You have no weapons on you. What do you do?",'Pick up the gun right next to you','Kick the zombie down and run','Cry in the corner while you await your death','Try to move a bookshelf to distance yourself from the zombie'], \
    'q8':[ 'What is the best means of transportation in an infected area?','Tank','Horse','bycicle','motorcycle'], \
    'q9':[ 'What would you do if someone close to you started to turn (into a zombie) in front of you?','Trap them and keep them in a secure location until they come out with a cure','Kill them','Let them free','Keep them captive and preform experiments on them'], \
    'q10':[ 'Which is NOT a term used as an alternative to "zombie"?','stalkers','walkers','roamers','biters'] \
    }  #dictionary of the questions in html form
#print questions


def helpDis(): #puts  'disabled' before each answer
    for q in questions:
        questions[q] = [questions[q][0]] + ['disabled'] + [questions[q][1]] + ['disabled'] + [questions[q][2]] + ['disabled'] + [questions[q][3]] + ['disabled'] + [questions[q][4]]
helpDis()

def helperIndex(q):  #translates a question answer to a number
    if q == 'a':
        return 1
    elif q == 'b':
        return 3
    elif q == 'c':
        return 5
    elif q == 'd':
        return 7
    else: 
        return None

def scoreMeaning(score): #another helper -- returns what your score means to you
    s =''
    if score <3:
        s += "You're basically dead already.  Don't even try."
    elif score <6:
        s += "You wouldn't survive a week out there.  You have the potential to learn but you aren't even close to being able to survive on your own"
    elif score <10:
        s += "Keep working at it, you're a sure survivor"
    elif score == 10:
        s += "Keep it up!  You're a born leader!"
    return s

def userAnswer(): #returns what yourr answers were and finds score
    s = '' #what will be returned in the end
    answers = {"q1":"d","q2":"b","q3":"b","q4":"c","q5":'a','q6':'d','q7':'b','q8':'d','q9':'b','q10':'a'}  # CHANGE WHEN NEW QUESTION
    score = 0 #keep track of points
    for question in d.keys():  #iterates though question responces and checks if correct
        if question != 'user' and question != 'magicnumber':

            if d[question] == answers[question]:
                score += 1
	        questions[question][0] = '+++ CORRECT +++ <br>' + questions[question][0]
            else:
                questions[question][0] = 'xxx WRONG xxx <br>' + questions[question][0]	
            questions[question][helperIndex(d[question])] = 'active'
    s += "You got " + str(score) + " out of 10 correct! <br>"
    s += scoreMeaning(score)
    return s
print userAnswer()

def viewAns():  #prints out questions and stuff
    s = '\n<br>\n<h3>Your answers</h3>\n<ol>'
    l = ["q1","q2","q3","q4","q5","q6","q7",'q8','q9','q10']
    for q in l:
        line = questions[q]
        s += '<li>' + line[0] + ' \n<ul>\n' 
        s += '<li id = "quiz"><label><input type="radio" name="' + q + '" value="a" ' + line[1]+ '>' + line[2] + '</label></li>'
        s += '<li id = "quiz"><label><input type="radio" name="' + q + '" value="b" ' + line[3]+ '>' + line[4] + '</label></li>'
        s += '<li id = "quiz"><label><input type="radio" name="' + q + '" value="c" ' + line[5]+ '>' + line[6] + '</label></li>'
        s += '<li id = "quiz"><label><input type="radio" name="' + q + '" value="d" ' + line[7]+ '>' + line[8] + '</label></li>'
        s += '\n</ul><br></li>'
    return s
print viewAns()

print  '''
</ol>

<br><br><br><br><br>
<p style="font-size: 10pt">Backgound Image Credit:  Walpaper Abyss</p>
</div>

</body>
</html>
'''
