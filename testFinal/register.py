#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

import cgi,cgitb,os,random,hashlib
cgitb.enable()

def header():
    return '''
<!DOCTYPE HTML>
<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Create account</title>
</head>
<body>

<div id="menu">
<span id="top">Are you prepared?</span>
<li id="nav"><a href="home.py">Home</a></li>
<li id="nav"><a href="tools.py">Equipment</a></li>
<li id="nav"><a href="quiz.py">Quiz</a></li>
<li id="nav"><a href="safehouses.py">Safehouses</a></li>
<br>
<span id="top">Account info</span>
<li id="nav">
<a href="login.html">Login</a>
</li>
<li id = "nav">    
<a class="active" href="register.html">Register</a>
</li>
</div>

<div id="right">
'''

def footer():
    return """</div></body>
</html>"""

def md5Pass(password):
    m = hashlib.md5()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('users.txt','r').readlines()
    for line in text:
        if line.split(",")[0]==user:
            return True
    return False

def valid(s):
    for c in s:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9'):
            return False
    return True

def createAccount(form):
    result =  "<br><div id = 'right' attempting to create an account...<br>"
    if "user" in form and "pass" in form and "pass2" in form:
        user = form['user'].value
        password = form['pass'].value
        password2 = form['pass2'].value
        if checkIfNameExists(user):
            result += "user exists: "+ user +"<br>"
        elif password != password2:
            result += "passwords do not match!<br> </div>"
        elif not valid(user):
            result += "username contains invalid characters<br> </div>"
        else:
            result += "account "+user+' created! login here: <a href="login.html">login page</a><br> </div>'
            f = open('users.txt','a')
            password = md5Pass(password+user)
            f.write(user+","+password+"\n")
            f.close()
    else:
        result+="<h1>Invalid form submission, please fill in all fields</h1> </div>"
    return result


def notFilledIn():
    return '''You need to create an account using the form found <a href="create.html">here</a>\n'''

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notFilledIn()
    else:
        body += createAccount(form)
    print header() + body + footer()

main()



