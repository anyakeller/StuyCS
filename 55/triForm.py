#!/usr/bin/python
# === LINE BELOW IS MAGIC TOO ===
print 'Content-Type: text/html\n'

# === MORE MAGIC ===
print ' ' #Sha-Bang!!!

#Team Trampoline -- Anya Keller, Sherry Dang
#IntroCS2 pd1
#HW55 - Going Formal
#2015-05-27

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

def store(): #stores the submitted information
	sides = {}
	try:
		for k in storage.keys(): #goes through the keys
			sides[k] = int(storage[k].value)
		return sides
	except:
		return None
sides =  store()
       
def herron(a,b,c):#fxn for area 
    s  = 0.5 * (a+b+c) #semiperimeter
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 #herron's formula 
    return area , (a+b+c) #two inputs(necessary for fxn math)

def perim(a,b,c): #fxn for perimeter
    return a+b+c


def math(sides):
    try:
        string = ''
        area , perim =  herron(sides['a'],sides['b'],sides['c'])
                         #fxn herron gives two inputs so area is equal to
                         #the first input and the second input is equal to perimeter.
        string += 'Area: '
        string += str(area)
        string += '<br>'
        string += 'Perimeter: '        
        string += str(perim)
        return string
    except: #if not a triangle
        return '<br>bad input'
print math(sides)


print '</p>'
print '</body>'
print '</center>'
print '</html>'
