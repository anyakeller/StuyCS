#team_team: Richard Lin, Anya Keller, Kenneth Ho
# IntroCS2 pd1
# HW16 -- Stringy Loops
# 2015-03-16

def addMultPrint(a,b):
    print "The sum of " + str(a) + " and " + str(b) + " is " + str(a + b)
    print "Their product is " + str (a * b)

addMultPrint(1 , 3)
#The sum of 1 and 3 is 4
#Their product is 3
addMultPrint(5 , 7)
#The sum of 5 and 7 is 12
#Their product is 35

def addMultHTML(a,b):
    print '<!DOCTYPE html>'
    print '<html>'
    print '<body>'
    print "The <i> sum </i> of " + str(a) + " and " + str(b) + " is <b> " + str(a + b) + ' </b>'
    print '<br>'
    print 'Their <i> product </i> is <b> ' + str (a * b) + ' </b>'
    print '</body>'
    print '</html>'

addMultHTML(1 , 3)
#<!DOCTYPE html>
#<html>
#<body>
#the <i> sum </i> of 1 and 3 is <b>  4 </b>
#<br>
#Their <i> product </i> is <b> 3 </b>
#</body>
#</html>

addMultHTML(5 , 7)
#<!DOCTYPE html>
#<html>
#<body>
#the <i> sum </i> of 5 and 7 is <b>  12 </b>
#<br>
#Their <i> product </i> is <b> 35 </b>
#</body>
#</html>

#sumDigits taken from hw15.py
def sumDigits(n):
    x = 0
    while n > 0:
        x = x + (n % 10)
        n = n // 10
    return x

def tablefy(n):
    print '<!DOCTYPE html>'
    print '<html>'
    print '<body>'
    print '<table border="1px">'
    print '     <tr>'
    print '         <th> n </th>'
    print '         <th> n^2 </th>'
    print '         <th> sumDigits </th>'
    print '     </tr>'
    rows = 1
    while rows <= n:
        print '     <tr>'
        print '         <td> ' + str(rows) + ' </td>'
        print '         <td> ' + str(rows ** 2) + ' </td>'
        print '         <td> ' + str(sumDigits(rows)) + ' </td>'
        print '     </tr>'
        rows += 1
    print '</table>'
    print '</body>'
    print '</html>'
    
tablefy(2)
#<!DOCTYPE html>
#<html>
#<body>
#<table border="1px">
#     <tr>
#         <th> n </th>
#         <th> n^2 </th>
#         <th> sumDigits </th>
#     </tr>
#     <tr>
#         <td> 1 </td>
#         <td> 1 </td>
#         <td> 1 </td>
#     </tr>
#     <tr>
#         <td> 2 </td>
#         <td> 4 </td>
#         <td> 2 </td>
#     </tr>
#</table>
#</body>
#</html>
