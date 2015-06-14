#!/usr/bin/python
print 'Content-Type: text/html\n'
print ' ' #Sha-Bang!!!
#here we go!!! 

file= open('questions.txt','r')
questions =  file.readlines()


print '''
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="style.css">
        <title>TEMPLATE</title>
    </head>
<body>

<div id="menu"> 
    <span id="top">Are you prepared?</span> 
        <li id="nav"><a href="index.html">Home</a></li> 
        <li id="nav"><a href="tools.py">Equipment</a></li> 
        <li id="nav"><a href="quiz.py">Quiz</a></li> 
	<li id="nav"><a class="active" href="template.py">Template</a></li>
        <br> 
    <span id="top">Account info</span> 
        <li id="nav"> 
            <a href = "login.html">Login</a> 
        </li> 
        <li id = "nav">     
            <a href = "register.html">Register</a> 
        </li> 
</div> 
    
<div id="right">
    <center><span id="name">The Zombie Survivor's Handbook</span></center>
    <h2>Page Title</h2>
</div>
</body>
</html>
'''
