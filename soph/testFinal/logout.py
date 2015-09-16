#!/usr/bin/python
print 'Content-type: text/html\n'
print ''

import cgi,cgitb,os
#cgitb.enable()
def header():
    return '''
<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Logging Out</title>
</head>
<body>
<div id="menu">
<span id="top">Are you prepared?</span>
    <li id="nav"><a href="home.py">Home</a></li>
    <li id="nav"><a href="tools.py">Equipment</a></li>
    <li id="nav"><a href="quiz.py">Quiz</a></li>
    <li id="nav"><a href="safehouses.html">Safehouses</a></li>
    <br>
    <span id="top">Account info</span>
    <li id="nav">
        <a href = "login.html">Login</a>
    </li>
    <li id = "nav">    
        <a href = "register.html">Register</a>
    </li>
</div>

    '''

def footer():
    return """</body>
</html>"""

#remove a user, only do this if they successfully authenticated
#since this does not check to see if you have the right person
def remove(user,magicnumber):
    text = open('loggedin.txt','r').read()
    result = "<div id = 'right'>User not logged out<br></div>\n"
    if (user+",") in text:
        #remove code
        outfile = open('loggedin.txt','w')
        lines = text.split('\n')
        for i in range(len(lines)):
            lines[i]=lines[i].split(",")
            if len(lines[i]) > 2:
                if(lines[i][0] != user or lines[i][1] != str(magicnumber) ):
                    outfile.write(','.join(lines[i])+"\n")
                else:
                    result = "<div id = 'right'>Logged out user<br>\n Click <a href='home.py'>here</a> to go to the home page!</div>"
        outfile.close();
    else:
        result = "<div id = 'right'>User not found<br>\n</div>"
    return result


def processForm(form):
    if( 'user' in form and 'magicnumber' in form):
        user = form.getvalue('user')
        mn = form.getvalue('magicnumber')
        return remove(user,mn)
    return "<div id = 'right'>You must be logged in properly to log out!<br>\n</div>"

def notLoggedIn():
    return "<div id = 'right'>You must be logged in before trying to log out!<br>\n</div>"

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notLoggedIn()
    else:
        body += processForm(form)
    print header() + body + footer()

main()
