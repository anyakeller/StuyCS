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
import os
inputs =  os.environ['QUERY_STRING'].split('&')

def inputSplit():
    sides = {}
    if inputs != ['']:
        for query in inputs:
            query = query.split('=')
            sides[query[0]] = int(query[1])
        return sides
    else:
        print 'No query string'
        
sides = inputSplit()

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

'''
#shows the os.environ dictionary
def sorting():
    for thing in os.environ:
        print thing + ' --- ' + os.environ[thing] + '<br>'
#sorting()
'''
print '</p>'
print '</body>'
print '</center>'
print '</html>'
