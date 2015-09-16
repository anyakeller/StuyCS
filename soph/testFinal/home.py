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
if 'magicnumber' in form:
    magicNumber = form['magicnumber'].value

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
<title>Home Page</title>
</head>

<body>


<div id="menu">
<span id="top">Are you prepared?</span>
<li id="nav"><a class="active" href="home.py''' + securefields() + '''">Home</a></li>
<li id="nav"><a href="tools.py''' + securefields() + '''">Equipment</a></li>
<li id="nav"><a href="quiz.py''' + securefields() + '''">Quiz</a></li>
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
            </li>
    </div>'''
    header += '''
<div id="right">
<center><span id="name">The Zombie Survivor's Handbook</span></center>
<p>Do you have what it takes to survive?
</p>
<p> 
    <h3>How to protect yourself</h3>
<p>When the virus hit, air and sea barriers didn't deter it from spreading.  Ever since the outbreak, survival became our primary goal.  The mysterious disease caused the dead to come back as bloodthirsty "walkers".  It's not only the dead that come back.  The disease lies dormant in everyone and anything that's alive.  Once you die, your body becomes the host to a new entity.  Endlessly wandering around in search of human flesh, a pack of roamers might come across a survivor.  If that survivor is you, you should be prepared.</p>

<p>We haven't been able to learn much about the zombies but we do know that the disease has something to do with the brain.  A zombie can keep walking even if it's missing half a ribcage and a jaw.  The only thing that stops them is a fatal blow to the head which damages the nervous system.  Take caution when choosing a weapon.  Guns are loud and have the potential to attract more zombies.  The best way to go is with a knife or shovel.</p>

<p>The only way to survive is to block out all emotion.  There will be some life changing (or ending) decisions you'll have to make and you'll have to do it fast.  If a loved one begins to reanimate, don't let your feelings get between you and the biter's skull.  Keeping them alive will do nothing but hurt you.  There is no cure so you're never getting them back.  The best thing to do for them is to let them rest in peace.</p>

</p>If you're in an infected zone, GET OUT.  The fastest means of transportation is a motorcycle so stay away from that armored tank!  If you're being cornered by a zombie you want to incapacitate them and run.  If you run first they'll slowly but surely catch up to you.  Zombies have an infinite amount of stamina so they'll follow you for as long as they know you're there.  Never get chased into a lake because zombies don't need to breathe.  They'll wait at the bottom until you can't keep swimming and you sink.</p>

<p>Keep a sharp mind and never let your guard down.
Good luck!</p>
</p>
<p>
    <h3>Quick Tips</h3>
    <ul>
        <li>Travel in small groups (3-5 people)</li>
        <li>Make sure you know where the nearest base is</li>
        <li>Avoid going out at night</li>
	<li>Try to remain quiet in any situation</li>
    </ul>
</p>
<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
<p style="font-size: 10pt">Backgound Image Credit:  Walpaper Abyss</p>
</div>
</body>

</html>
'''
    return header
print header()
