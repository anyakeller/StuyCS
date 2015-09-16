#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

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
        return "?user="+user+"&magicnumber="+magicnumber + "&"
    return ""
    
query = FStoD()

tool1 = None
tool2 = None
tool3 = None
tool4 = None
tool5 = None
tool6 = None
tool7 = None
tool8 = None
tool9 = None
tool10 = None
#Set the tools equal to the tool that is currently in the query for that specific variable
if query.has_key("tool1"):
    tool1 = query["tool1"]
if query.has_key("tool2"):
    tool2 = query["tool2"]
if query.has_key("tool3"):
    tool3 = query["tool3"]
if query.has_key("tool4"):
    tool4 = query["tool4"]
if query.has_key("tool5"):
    tool5 = query["tool5"]
if query.has_key("tool6"):
    tool6 = query["tool6"]
if query.has_key("tool7"):
    tool7 = query["tool7"]
if query.has_key("tool8"):
    tool8 = query["tool8"]
if query.has_key("tool9"):
    tool9 = query["tool9"]
if query.has_key("tool10"):
    tool10 = query["tool10"]

#Making the drop down menu
def renderOption(toolName, toolnumber):
    startTag = "<option>"
    if toolName == toolnumber:
        startTag = "<option selected>"
    return startTag + toolName + "</option>\n"

def header():
    header = '''
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="style.css">
    <title>Equipment</title>
    </head>
    
    <body>
    
    
    <div id="menu">
        <span id="top">Are you prepared?</span>
            <li id="nav"><a href="home.py''' + securefields() +  '''">Home</a></li>
            <li id="nav"><a class="active" href="tools.py''' + securefields() +  '''">Equipment</a></li>
            <li id="nav"><a href="quiz.py''' + securefields() + '''">Quiz</a></li>
	    <li id="nav"><a href="safehouses.py''' + securefields() + '''">Safehouses</a></li>    
<br>
        <span id="top">Account info</span>
<li id="nav">'''
        
    if 'user' in form and form['user'].value != "":
        header += "<center>" + remove(user) + "</center>"
        header += '''<a href="logout.py''' + securefields() + '''">Logout</a><br></div>'''
        
    else:
        header += '''
            <li id="nav">
                <a href = "login.html''' + securefields() +  '''">Login</a>
            </li>
            <li id = "nav">    
                <a href = "register.html''' + securefields() +  '''">Register</a>
            </li>
    </div>'''
    header += '''
    <div id="right">
        <center><span id="name">The Zombie Survivor Handbook</span><br>
        <h1>Take a Tools Test!</h1>
        <p>If you guess the name of the tool, you'll find out how you can use it and why it's useful.</p></center>
        
    <table border = "10" bordercolor = "#800000" cellpadding = "10px" align = "center" width = 1000>
    <tr>
        <th width = "30%"><b>Tool</b></th>
        <th width = "20%"><b>Name</b></th>
        <th>
            <b>Description</b>
        </th>
    </tr>
<form name = "input" method="GET" action = "tools.py''' + securefields() + '''">
<select hidden name = "user"><option>''' + user + '''</option></select>
<select hidden name = "magicnumber"><option>''' + magicNumber + '''</option></select>
'''
    return header

#Each row of the table consists of an image, a drop down menu, and a description
def makerow(image, description, toolNumber, toolquoted):
    return '''
            <tr><td><center>
            ''' + image + '''
            </center></td>
            <td>
            <select name ="''' + toolquoted + '''" size = "1">
            ''' + renderOption("Crossbow", toolNumber) + '\t\t\t'\
                + renderOption(".357 Magnum", toolNumber) + '\t\t\t'\
                + renderOption("M67 Grenade", toolNumber) + '\t\t\t'\
                + renderOption("M2 Flamethrower", toolNumber) + '\t\t\t'\
                + renderOption("Water Filter", toolNumber) + '\t\t\t'\
                + renderOption("Tomahawk", toolNumber) + '\t\t\t'\
                + renderOption("Thompson", toolNumber) + '\t\t\t' \
                + renderOption("Machete", toolNumber) + '\t\t\t' \
                + renderOption("M1897 Trench Gun", toolNumber) + '\t\t\t' \
                + renderOption("Silencer", toolNumber) + '\t\t\t' + \
            '''
            </select><br>
            </td>
            <td><center>
            ''' + description + '''
            </center>
            </td>
            </tr>
        '''
        

def footer():
    return ''' 
        </table><br>
        <center><p><b><u>TIP: Always aim for the head (where the brain is located)</u></b></p></center>
<center><input type = "submit" name = "submit&''' + securefields() +  '''"></center>
            <br><br><br>
        </form>
    </div><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
    <p style = "font-size: 10pt">
    Image and Information Credits go to Call of Duty Wikia<br>Credit to Wilson Berkow for some help with the code (overcoming an obstacle).</p>
    </body>
    </html>'''

#This is where the entire page is generated
def fillTemplate(description, description2, description3, description4, description5, description6, description7, description8, description9, description10):
    return header() \
    + makerow('<img height = "100" src = "Tomahawk.webp">', description, tool1, "tool1") \
    + makerow('<img height = "100" src = "machete.png">', description2, tool2, "tool2") \
    + makerow('<img height = "100" src = "357_magnum.png">', description3, tool3, "tool3") \
    + makerow('<img height = "100" src = "M1897_Trench_Gun_model.png">', description4, tool4, "tool4") \
    + makerow('<img height = "100" src = "Crossbow.png">', description5, tool5, "tool5") \
    + makerow('<img height = "100" src = "water filter.jpg">', description6, tool6, "tool6") \
    + makerow('<img height = "100" src = "Silencer.png">', description7, tool7, "tool7") \
    + makerow('<img height = "100" src = "M67 Grenade.png">', description8, tool8, "tool8") \
    + makerow('<img height = "100" src = "M2 Flamethrower.png">', description9, tool9, "tool9") \
    + makerow('<img height = "100" src = "Thompson.png">', description10, tool10, "tool10") \
    + footer()

#Checking for the matching descriptions
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def givedescription(val1):
    if val1 == "Tomahawk": #d.has_key("tool1") and d["tool1"] == "Tomahawk":
        return "It instantly kills any zombie it hits. Unlike the Throwing Knife, however, the Tomahawk always bounces off walls and floors when thrown, making ricochet kills, or 'bank shots,' a more likely possibility. "
    else:
        return "Nope, this is not it"
def givedescription2(val2):
    if val2 == "Machete":
        return "This machete can be very useful for killing zombies in close range. Aim for the head, specifically the brain, which will instantaneously kill the zombie."
    else:
        return "Nope, this is not it"
def givedescription3(val3):
    if val3 == ".357 Magnum":
        return "This pistol is a powerful sidearm for those who want to take down the enemy in the least amount of shots. It has a fast reload rate with low ammo storage."
    else:
        return "Nope, this is not it"
def givedescription4(val4):
    if val4 == "M1897 Trench Gun":
        return "This shotgun has a very slow rate of fire and slow reload with a relatively small ammo pack, but it does have very high damage with little recoil. It reloads by pump-action."
    else:
        return "Nope, this is not it"
def givedescription5(val5):
    if val5 == "Crossbow":
        return "This weapon requires great precision, accuracy, and additional arrows in order to kill zombies. It is more suited for zombies that are farther away."
    else:
        return "Nope, this is not it"
def givedescription6(val6):
    if val6 == "Water Filter":
        return "This water filter can be useful for getting germs out of water. Water might be scarce in some regions. The water you do find might be contaminated. This can be useful."
    else:
        return "Nope, this is not it"
def givedescription7(val7):
    if val7 == "Silencer":
        return "This can be very useful when you want to shoot a zombie, but you don't want to attract other zombies. If you add this to the front of a gun, it will silence the shot when it is fired."
    else:
        return "Nope, this is not it"
def givedescription8(val8):
    if val8 == "M67 Grenade":
        return "This is an all-rounded grenade that can be used when you encounter a huge crowd of zombies. Be careful, however, when using this because the loud noise it makes can attract other zombies and all of the zzombies may not be killed, as you have destroy their brains for that to happen."
    else:
        return "Nope, this is not it"
def givedescription9(val9):
    if val9 == "M2 Flamethrower":
        return "LIGHT SOME ZOMBIES ON FIREEEE!!! Caution: Use with care you may burn yourself. Allow this to cool down a bit after usage."
    else:
        return "Nope, this is not it"
def givedescription10(val10):
    if val10 == "Thompson":
        return "This has a fast rate of fire. Make sure to be aware of the high recoil of the gun before using it, so you won't knock yourself over everytime you shoot. This gun can cause a high level of damage and reloads very quickly."
    else:
        return "Nope, this is not it"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#print givedescription()
def main():
    if tool1 != None and tool2 != None and tool3 != None and tool4 != None and tool5 != None and tool6 != None and tool7 != None and tool8 != None and tool9 != None and tool10 != None:
        print fillTemplate(givedescription(tool1), givedescription2(tool2), givedescription3(tool3), givedescription4(tool4), givedescription5(tool5), givedescription6(tool6), givedescription7(tool7), givedescription8(tool8), givedescription9(tool9), givedescription10(tool10))
    else:
        print fillTemplate("", "", "", "", "", "", "", "", "", "")
main()
