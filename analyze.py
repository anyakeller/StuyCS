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
</style>
<title>Burough High School Evaluations vs Average Brough SAT Grades </title>
<body style="color:white;background: black;">
<center>
<head><a href="table.html"> Burough High School Evaluations</a> vs <a href="sta\
tsSAT.html"> Average Brough SAT Grades </a></head> <br><br>
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
            gradeDic[row[1][2]] += [ int(num[0]) + ( int(num[1]) / (10.0 ** (le\
n(num[1]))))]
    return gradeDic ,satDic

gradeDic, satDic= getNums(sat,grade)
def meanFind(nums):
    return 1.0 * sum(nums)/len(nums)

def meanThing(d):
    d = d
    for key in d:
        d[key] = meanFind(d[key])
    return d
satDic = meanThing(satDic)
gradeDic = meanThing(gradeDic)

def tableCompare(d1,d2):
    tablehtml =''
    tablehtml += '<table border="1px"> Data </tr>'
    tablehtml += '<tr colspan="3"> '
    for bur in d1:
        tablehtml += '\n\t<tr>'
        tablehtml += '\n\t\t<td><b>' + bur + '</b></td>'
        tablehtml += '\n\t\t<td>' + str(d1[bur]) + '</td>'
        tablehtml += '\n\t\t<td>' + str(d2[bur]) + '</td>'
	tablehtml += '\n\t</tr>'
    return tablehtml
tablehtml += tableCompare(satDic,gradeDic)

tablehtml+= '''
</center>
</html>
'''

file.write(tablehtml)
file.close()
satOpen.close()
gradeOpen.close()



    
