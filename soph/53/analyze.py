file = open('analysis.html','w')
satOpen = open('statsSAT.html','r')
gradeOpen = open('table.html','r')
sat = satOpen.read()
grade = gradeOpen.read()


tablehtml ='''
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
<title>Burough High School Evaluations vs Average Brough SAT Grades </title>
<body style="color:white;background: black;">
<center>
<head><a href="table.html"> Burough High School Evaluations</a> vs <a href="statsSAT.html"> Average Brough 2014 SAT Grades </a></head> <br><br>
<p>
Q = Queens <br>
X = The Bronx <br>
K = King's County (Brooklyn) <br>
R = Ritchmond County (Staten Island) <br>
M = Manhattan <br>
</p>

'''

def getNums(sat,grade):
    satDic = {'M':[],'X':[],'K':[],'Q':[],'R':[]}
    gradeDic = {'M':[],'X':[],'K':[],'Q':[],'R':[]}
    sat = "".join(sat.split('\t'))
    grade = "".join(grade.split('\t'))
    sat = "".join(sat.split('\n'))
    grade = "".join(grade.split('\n'))
    sat = sat.split('<tr>')[1:-2]
    grade = grade.split('<tr>')[1:]
    for row in sat:
        if 's' not in row:
            row = row.split('<td>')
            try:
                satDic[row[1][2]] += [int(row[6][:2])]
            except:
                satDic[row[1][2]] += [int(row[6][:3])]
    for row in grade:
        row = row.split('<td>')
        row[6] = row[6].strip('<>td/')
        if '.' not in row[6]:    
            try:
                gradeDic[row[1][2]] += [int(row[6][:2])]
            except:
                print 'naaa'
        else:
            num = row[6].split('.')
            gradeDic[row[1][2]] += [ int(num[0]) + ( int(num[1]) / (10.0 ** (len(num[1]))))]
    return gradeDic ,satDic

gradeDic, satDic= getNums(sat,grade)

def meanThing(d):
    d = d
    for key in d:
        d[key] = 1.0 * sum(d[key])/len(d[key])
    return d
satDic = meanThing(satDic)
gradeDic = meanThing(gradeDic)


def tableCompare(d1,d2):
    tablehtml =''
    tablehtml += '<table border="1px"> Data </tr>'
    tablehtml += '<th> Burough </th> <th>DOE Grade</th> <th>SAT Score (reading)</th>' 
    for bur in d1:
        tablehtml += '\n\t<tr>'
        tablehtml += '\n\t\t<td><b>' + bur + '</b></td>'
        tablehtml += '\n\t\t<td>' + str(d1[bur]) + '</td>'
        tablehtml += '\n\t\t<td>' + str(d2[bur]) + '</td>'
        tablehtml += '\n\t</tr>'
    tablehtml += '</table><br><br>'
    return tablehtml
tablehtml += tableCompare(gradeDic,satDic)

def graph(d1,d2):
        top = max(max(d1.values()),max(d2.values()))
        s = ''
	ordered = ['Q','X','K','R','M']
        while top >  0:
                for bur in ordered:
                        if d1[bur] >= top:
                                s += '* '
                        else:
                                s += '  '
                        if d2[bur] >= top:
                                s += '^  '
                        else:
                                s += '   '
                s += '\n'
                top -= 1
        s +=  '---' + '--' * len(d1.values()+d2.values()) + '\n'
        for bur in ordered:
                s += bur + '    '
	return s
tablehtml += '''
<p>
<br>
Veritcal bar Graph Representation <br>  
* = DOE Grade <br>
^ = Reading SAT Score <br>
</p>
'''
tablehtml += '<pre>' + graph(gradeDic,satDic) + '</pre>' 

tablehtml+= '''
</center>
</html>
'''


file.write(tablehtml)
file.close()
satOpen.close()
gradeOpen.close()
