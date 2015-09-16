# Anya Keller                                                                   
# IntroCS2 pd1                                                                  
# HW46 -- CSV -> HTML                                                           
# 2015-05-13                                                                    

testData = open('testdata.csv','r')
html = open('table.html', 'w')

#gets it started                                                                
tablehtml = '<!DOCTYPE html> \n<html>\n<body style="color:white;background: bla\
ck;">\n<center>\n<head><h1> CSV to HTML WOOHOO </h1></head>\n<p>#blackAndWhiteA\
llDayErryDay</p>\n<table border="1px">\n'
data = testData.readlines()
#creates the table                                                              
for row in data:
    l = row.strip('\n')
    l = l.split(',')
    tablehtml += '\n\t<tr>'
    for col in l:
        tablehtml += '\n\t\t<td>' + col + '</td>'
    tablehtml += '\n\t</tr>'
#ends the table                                                                 
tablehtml += '\n</table>\n</center>\n</body>\n</html>\n'


#writes and closes files                                                        
html.write(tablehtml)
testData.close()
html.close()
