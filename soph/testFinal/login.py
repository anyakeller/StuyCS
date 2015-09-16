#!/usr/bin/python
print 'Content-type: text/html\n'
print ''

import cgi,cgitb,os,random,hashlib

#cgitb.enable()

def header():
    return '''
<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Login</title>
</head>
<body>

<div id="menu"> 
    <span id="top">Are you prepared?</span> 
        <li id="nav"><a href="home.py">Home</a></li> 
        <li id="nav"><a href="tools.py">Equipment</a></li> 
        <li id="nav"><a href="quiz.py">Quiz</a></li> 
	<li id="nav"><a href="safehouses.py">Safehouses</a></li>
        <br> 
</div>
'''
    
def footer():
    return """</body>
</html>"""

def md5Pass(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('users.txt', 'r').readlines()
    print text
    for line in text:
        if line.split(",")[0]==user:
            return True
    return False

def authenticate(user,password):
    password = md5Pass(password+user) # you can make this different, but still unique md5Pass(password+user)
    text = open('users.txt', 'r').readlines()
    for line in text:
        line = line.strip().split(",")
        if line[0]==user:
            if line[1]==password:
                return True
            else:
                return False
    return False

#the following code takes care of making sure the user is recognized
#as being logged in on other parts of the website
#remove a user, only do this if they successfully authenticated
#since this does not check to see if you have the right person
def remove(user):
    infile = open('loggedin.txt','r')
    text = infile.read()
    infile.close()
    if (user+",") in text:
        #remove code
        outfile = open('loggedin.txt','w')
        lines = text.split('\n')
        for i in range(len(lines)):
            lines[i]=lines[i].split(",")
            if len(lines[i]) > 1:
                if(lines[i][0] != user):
                    outfile.write(','.join(lines[i])+'\n')
        outfile.close();

#only meant to be run after password authentication passes.
#uses call to remove(user) that will remove them no matter what.
def logInUser(username):
    magicNumber = str(random.randint(1000000,9999999))
    remove(username)
    outfile = open('loggedin.txt','a')
    IP = "1.1.1.1"
    if "REMOTE_ADDR" in os.environ :
        IP = os.environ["REMOTE_ADDR"]
    outfile.write(username+","+magicNumber+","+IP+"\n")
    outfile.close()
    return magicNumber

def login(form):
    result = "<br><p><div id = 'right'>"
    if not ('user' in form and 'pass' in form):
        return "<p><br><div id = 'right'>Username or password not provided</div></p>"
    user = form['user'].value
    password = form['pass'].value
    if authenticate(user,password):
        result += "Success!<br>"
        #add user to logged in status
        magicNumber = logInUser(user)
        result += '<a href="home.py?user='+user+'&magicnumber='+str(magicNumber)+'">Click here to go to the home page!</a></div></p>'
    else:
        result += "Failed to log in, authentication failure</div></p>"
    return result

def notLoggedIn():
    return '''<div id = 'right'> You need to login, <a href="login.html">here</a>\n</div>'''

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notLoggedIn()
    else:
        body += login(form)
    print header() + body + footer()

main()
