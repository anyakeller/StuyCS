#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

import cgi
import cgitb
cgitb.enable()

#outStream = open('safehouses.html', 'w')
#outStream.write("<!DOCTYPE html> <html>")
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
        html += "<p style = 'font-size:20'>Hello<br>" + user + "!</p>"
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

def header():
    header = '''
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="style.css">
    <title>Safehouses</title>
    </head>
    
    <body>
    
    <div id="menu">
        <span id="top">Are you prepared?</span>
            <li id="nav"><a href="home.py''' + securefields()  +'''">Home</a></li>
            <li id="nav"><a href="tools.py''' + securefields() +'''">Equipment</a></li>
            <li id="nav"><a href="quiz.py''' + securefields() + '''">Quiz</a></li>
            <li id="nav"><a class = "active" href="safehouses.py''' + securefields() + '''">Safehouses</a></li>
    <br>
        <span id="top">Account info</span>'''
    if 'user' in form:
        header += "<center>" + remove(user) + "</center>"
        header += '''<li id = "nav"><a href="logout.py''' + securefields() + '''">Logout</a></li><br>'''
        
    else:
        header += '''
            <li id="nav">
                <a href = "login.html">Login</a>
            </li>
            <li id = "nav">    
                <a href = "register.html">Register</a>
            </li>'''
    header += '''</div>
    <div id="right">
        <center><span id="name">The Zombie Survivor Handbook</span><br>
        If you find yourself in Chicago during the apocalypse, here's a handy table to see the 328 nearby safehouses.
        </div>'''
    return header

def openfile():
    inStream = open('311_Service_Requests_-_Vacant_and_Abandoned_Buildings_Reported.csv', 'r')
    fileread = inStream.readlines()
    for line in fileread:
        line = line.strip()
    inStream.close()
    return fileread

def annoyingcommas(quoted):
    L1 = quoted.split('"')
    L1[1] = L1[1].replace(',', '')
    L1 = ''.join(L1)
    return L1
    
def tablefy():
    fileread = openfile()
    table = "<div id = 'right'><br><br><br><br><br><table border = '10' bordercolor = '#A00000'>"
    i = 0
    for line in fileread[0:328]:
        if line[1] != ',':
            if '"' in line:
                line = annoyingcommas(line)
    #Go through the list of the file contents line by line and split by the commas
            line = line.split(",")
            table +='<tr>'
    #Place each sublist in a table row
            for element in line[0:15]:
                if line != '':
        #Go through sublists and place each element in a table cell.
                    table += '<td>' + element + '</td>'
            table += '</tr>'
    table += "</table>"
    return table
print header() + tablefy() +"<br><br><p style = 'font-size:10pt'> This data was obtained from data.gov. <a class = 'footnote' href = 'http://catalog.data.gov/dataset/311-service-requests-vacant-and-abandoned-buildings-reported-13f8e'>Here's the link</a></p></div></body></html>"


#outStream.write(header() + tablefy() + "<br><br><p style = 'font-size:10pt'> This data was obtained from data.gov. <a class = 'footnote' href = 'http://catalog.data.gov/dataset/311-service-requests-vacant-and-abandoned-buildings-reported-13f8e'>Here's the link</a></p></div></body></html>")
#outStream.close()
