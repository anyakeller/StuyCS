#!/usr/bin/python
# ========= HASHBANG LINE ABOVE IS MAGIC! =========
# ========= (Must be first line of file.) =========

import cgi
import cgitb
cgitb.enable()  #diag info --- comment out once full functionality achieved

'''
Cool Stuff
-Takes punctuation and non-ascii characters
-My regular b&w default coloring
-You can change the color of your mesage!!!
-centered
'''


# ~~~~~~~~~~~~~~~ support functions ~~~~~~~~~~~~~~~
def FStoD():
    '''
    Converts cgi.FieldStorage() return value into a standard dictionary
    '''
    d = {}
    formData = cgi.FieldStorage()
    for k in formData.keys():
        if type(formData[k]) == list:
            d[k] = formData[k]
        else:
            d[k] = formData[k].value
    return d
d = FStoD()

def expand():
    l = []
    for el in d['sty']:
        l += el.value
    return ''.join(l) 

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#eyyyy leti's give it up for anya's ugly rot13 code from 3/26/15!!!
#from previous hw
def rotShiftChr(ch, shift): #character, shift
    value = ord(ch)
    if 65 <= value <= 90:  #upper case sturfff
        value +=shift
        if value > 90:
            value = 65 + (value - 91)
    elif 97 <= value <= 122:    #upper case
        value +=shift
        if value > 122:
            value = 97 + (value - 123)
    else:
        return ch   #punctuation stuff
    return chr(value)


#heh i did this already
def rot13(phr):
    new = ''
    count = 0
    for ch in phr:
        if ch.isalpha():
            new += rotShiftChr(ch,13)
        else:
            new += ch
    return new

# ======== PHEW! I'm GLAD THAT'S OVER! ===========
# ========= CONTENT-TYPE LINE REQUIRED. ===========
# ======= Must be beginning of HTML string ======== 
htmlStr = "Content-Type: text/html\n\n" #NOTE there are 2 '\n's !!! 
htmlStr += "<html><center><head><title> Encrypted Message </title></head></html>\n"
htmlStr += '<body style="color:white; background: black;">'
# ~~~~~~~~~~~~~ HTML-generating code ~~~~~~~~~~~~~~
htmlStr += "<h1>Encrypted message</h1>"
#htmlStr += str( d )
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def encr(d):
    s = '<p style="color:' + d['color'] + ';">'
    if d['encr'] == 'reverse':
        s +=  d['message'][::-1]
    else:
	s += rot13(d['message']) 
    
    if 'sty' in d:
        sty = expand()
        s += 'hey'   
        if 'b' in sty:
            s = '<b>' + s + '</b>'
	if 'u'in sty:
            s = '<u>' + s + '</u>'
	if 'i' in sty:
            s = '<i>' + s + '</i>'
	if 'pre' in sty:
	    s = '<pre>' + s + '</pre>'
    s += '</p>'
    return s
htmlStr += encr(d)

htmlStr += "</body></center></html>"

print htmlStr
