# Anya Keller                                                                   
# IntroCS2 pd1                                                                  
# HW46 -- CSV -> HTML                                                           
# 2015-05-13                                                                    

testData = open('data.csv','r')
html = open('table.html', 'w')

#gets it started                                                                
tablehtml = '''
<!DOCTYPE html> 
<html>
<style>
    a {
        color: white;
    }
    a:link {
        text-decoration: underline;
    }
    a:visited {
        text-decoration: none;
    }
    a:hover {
        text-decoration: bold;
        color: #E5E5E5;
    }
</style>

<title>NYC School Grades </title>
<body style="color:white;background: black;">
<center>
<head><h1> NYC School Grades</h1></head>
<p><a href="https://data.cityofnewyork.us/Education/School-Progress-Report-2006-2007/weg5-33pj">Source: NYC Open Data </a></p>
<p>#blackAndWhiteAllDayErryDay</p>
<table border="1px">\n'''
data = testData.readlines()
#creates the table         
def head():    
    tablehtml = ''
    l = data.pop(0)
    l = l.strip('\n')
    l = l.split(',')
    for el in l:      
        tablehtml += '<th>'
        tablehtml += el
        tablehtml += '</th>'
    return tablehtml
tablehtml += head()
  

for row in data:
    if 'High School' in row:     
        row = row.strip('\n')
        row = row.split(',')
        tablehtml += '\n\t<tr>'
        while len(row) > 14:
            row[2] = row[2] + row[3]
            del row[3]
        for col in row:
            col = col.strip('"')
            tablehtml += '\n\t\t<td>' + col + '</td>'
        tablehtml += '\n\t</tr>'
#ends the table                                                                 
tablehtml += '\n</table>\n</center>\n</body>\n</html>\n'


#writes and closes files                                                        
html.write(tablehtml)
testData.close()
html.close()
