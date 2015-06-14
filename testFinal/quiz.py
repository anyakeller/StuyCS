#!/usr/bin/python
print 'Content-Type: text/html\n'
print ' ' #Sha-Bang!!!
#here we go!!! 

import cgi
import cgitb
cgitb.enable()

# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
form = cgi.FieldStorage()

def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        d[k] = formData[k].value
    return d

query = FStoD()

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
else:
    user = ""
if 'magicnumber' in form:
    magicNumber = form['magicnumber'].value
else:
    magicNumber = ""
def securefields():
    if 'user' in form and 'magicnumber' in form:
        user = form['user'].value
        magicnumber = form['magicnumber'].value
        return "?user="+user+"&magicnumber="+magicnumber
    else:
        return ""

file= open('questions.txt','r')
questions =  file.readlines()


def header():
    header = ''' 
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <script src="quiz.js"></script>
        <title>Quiz</title>
    </head>
<body>

<div id="menu"> 
    <span id="top">Are you prepared?</span> 
<li id="nav"><a href="home.py''' + securefields() + '''">Home</a></li>
<li id="nav"><a href="tools.py''' + securefields() + '''">Equipment</a></li>
<li id="nav"><a class = "active" href="quiz.py''' + securefields() + '''">Quiz</a></li>
<li id="nav"><a  href="safehouses.py''' + securefields() + '''">Safehouses</a></li>
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
    <h2>So You Think You know About Zombies?</h2>
    <form method="GET" action="quiz2.py''' + securefields() + '''" onsubmit="return validateForm()">
    <ol>'''
    return header
print header()
print ''.join(questions)  #I wrote a python file that appends html formatted questions to a txt file

print '''
    </ol>
<form method="GET" action="quiz.py''' + securefields() + '''">
<select hidden name = "user"><option>''' + user + '''</option></select>
<select hidden name = "magicnumber"><option>''' + magicNumber + '''</option></select>

    <input id="submit" type="submit" value="Submit Answers">
    </form>
    </form>    
<br><br><br><br><br>
<p style="font-size: 10pt">Backgound Image Credit:  Walpaper Abyss</p>
</div>
</body>
</html>
'''

file.close()
