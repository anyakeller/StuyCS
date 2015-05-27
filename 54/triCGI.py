#!/usr/bin/python
# === LINE BELOW IS MAGIC TOO ===
print 'Content-Type: text/html\n'

# === MORE MAGIC ===
print ' ' #Sha-Bang!!!
print '<html>'
print '<center>'
print '<title> Look! Query Stuff!    </title>'
print '<body style="color:white;background: black;">'
print '<head> OMG Query Stuff!!!  </head> <br><br>'    
print '<p>'

#WRITE CODESTUFF HERE
import cgi
import cgitb

#cgitb.enable()


storage  = cgi.FieldStorage()

def store():
	sides = {}
	try:
		for k in storage.keys():
			sides[k] = int(storage[k].value)
		return sides
	except:
		return None
sides =  store()
       
def herron(a,b,c):
    s  = 0.5 * (a+b+c)
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 
    return area , (a+b+c)

def perim(a,b,c):
    return a+b+c


def math(sides):
    try:
        string = ''
        area , perim =  herron(sides['a'],sides['b'],sides['c'])
        string += 'Area: '
        string += str(area)
        string += '<br>'
        string += 'Perimeter: '        
        string += str(perim)
        return string
    except:
        return '<br>bad input'
print math(sides)


print '</p>'
print '</body>'
print '</center>'
print '</html>'
