# Anya Keller
# IntroCS2 pd1
# HW19 -- Slice, Dice, Replace
#2015-03-23 


def tablefyASCII():
    
    #initialization
    print "<!DOCTYPE html>"
    print "<hmtl>"
    print "     <title>"
    print "         Slice, Dice, Replace"
    print "     </title>"
    print "<body>"
    print "<h1>"
    print "     Slice, Dice, Replace"
    print "</h1>"
    print '<table border="1px" align="center">'
    print '<tbody>'
    print '<tr style="color: #FFFF33;">'
    print '     <th> Letter </th> <th> number </th>'
    print '</tr>'
    #end of initialization

    #beginning of stuff
    upper = 65  #to 90
    lower = 97 #to 122
    
    
    #upper case
    while upper <= 90:     
        print '<tr>'
        print '     <td> ' + str(chr(upper)) + ' </td>'
        print '     <td> ' + str(upper) + ' </td>'
        print '</tr>'
        upper += 1
        
    #lower case
    while lower <= 122:
        print '<tr>'
        print '     <td> ' + str(chr(lower)) + ' </td>'
        print '     <td> ' + str(lower) + ' </td>'
        print '</tr>'  
        lower += 1

    print '</tbody>'
    print '</table>'
    print '</body>'
    print '</html>'
    

#tablefyASCII()


#coding bat

#Logic-1
def near_ten(num):
    if num % 10 <= 2 or num % 10 >= 8:
        return True
    else:
        return False
        