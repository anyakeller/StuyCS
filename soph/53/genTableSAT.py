# Anya Keller                                                                   
# IntroCS2 pd1                                                                  
# HW48 -- How Many Numbers Could a Thinker Crunch, if a Thinker Could Crunch Numbers?
# 2015-05-14                  
'''
My code is finished and now I broke it into sepparate functions so it is easier to modify and debug
'''

#handles first column titles
def firstColumn(tablehtml):
    firstrow = data[0].strip(' ,"\n\r') #gets rid of annoying commas in the beginnning and end
    firstrow = ['School Code'] + firstrow.split(',')
    for title in firstrow:
        tablehtml += '<th> '+ title +' </th>'
    tablehtml += '\n'
    return tablehtml

#fixes comma problems
def commaFix(row):
    #if the row is too long the isue is usually with a comma in in a school name unless its bktech wich has a comma in one of it's values
    while len(row) > 6:
        if 'BROOKLYN TECHNICAL HIGH SCHOOL' in row[1]: #lol bktech
            row[2] =  row[2] + row[3]
            del row[3]
        else:
            row[1] = row[1] + ',' + row[2]
            del row[2]
    return row


#tableifies the rest 
def tableifyRest(data,tablehtml):
    nums = [[],[],[],[]]
    for row in data[1:]:
        row = row.strip(' ,"\n\r')
        row = row.split(',')
        #fixes problems caused by commas in school names
        row = commaFix(row)
        #makes the table
        if row != ['']:
            tablehtml += '\n\t<tr>'
            pos = 0
            for element in row:
                element = element.strip('"')  
                if element != 's':
                    if pos >= 2:
                        nums[pos-2] = nums[pos-2] + [int(element)]
                pos += 1
                if pos == 6:
                    pos = 0
                elif ', THE' in element:
                    element = 'THE ' + element[:element.find(', THE') ] + element[(element.find(', THE') + 5):] 
                tablehtml += '\n\t\t<td>' + element + '</td>'
            tablehtml += '\n\t</tr>'
    return nums, tablehtml



#median stuff
def medianFind(nums):
    medians = ['medians']
    for block in nums:
        block.sort()
        if len(block) % 2 == 0:
            medians += [block[len(block)/2]]
        else:
            medians += [(block[len(block)/2] + nums[0][(len(block)/2) + 1])/2]
    return medians

#mean stuff
def meanFind(nums):
    means = ['means']
    for block in nums:
        tot = 0
        for num in block:
            tot += num
        means += [tot/len(block)]
    return means

#does math things
def mathThing():
    tablehtml = ''
    #for the mathy things
    maths = []
    maths += [medianFind(nums)]
    maths += [meanFind(nums)]
    for math in maths:
        tablehtml +=  '''
            <tr>
                <td></td>
                <td><b>''' + math.pop(0) + '</b></td>'
        for n in math:
            tablehtml += '''
                <td>''' + str(n) + '</td>'
        tablehtml += '\n\t</tr>'
    return tablehtml



SATdata = open('data_SAT2014.csv','r')
file = open('statsSAT.html', 'w')
data = SATdata.readlines()    
#gets html code started and begins table
tablehtml = '''
<!DOCTYPE html> 
<html>
<body style="color:white;background: black;">
<center>
<head><h1> 2014 New York SAT data </h1></head>
<p>This is a record of the SAT data from high schools in NYC.  High schools with less than 4 persons taking the test were omitted from this list.</p>
<table border="1px">
'''
#adds the <th> row 
tablehtml = firstColumn(tablehtml)
#adds the the rest of the list and retuns the values of each collumn
nums, tablehtml = tableifyRest(data, tablehtml)
#adds 
tablehtml += mathThing()
#closes rest of tags 
tablehtml += '''
</table>
</center>
</body>
</html>
'''
#writes and closes files                                                        
file.write(tablehtml)
SATdata.close()
file.close()

