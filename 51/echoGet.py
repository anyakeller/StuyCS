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

#WRITE CODESTUFF HERE
import os
inputs =  os.environ['QUERY_STRING'].split('&')
 

def inputSplit():
     if len(inputs) != 0:
          for query in inputs:
               print query
               print '<br>'
     else:
          print 'No query string'
inputSplit()


#shows the os.environ dictionary
def sorting():
    for thing in os.environ:
        print thing + ' --- ' + os.environ[thing] + '<br>'
#sorting()



print '</body>'
print '</center>'
print '</html>'
