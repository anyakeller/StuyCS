# Anya Keller                                                                   
# IntroCS2 pd1                                                                  
# HW47 -- (Almost) Crunching Real Numbers
# 2015-05-14                  
'''
OMG WHAT IS GOING ON WHYYYY IS IT DOING THE WEIRD THING WITH THE  'THE's AND ALL THAT UGHHH WHY THIS IS NOT OKAY AT ALLLLLLLLLL
NUUUUU
#brute force this shiz

One problem I did overcome is the extra comma problem is by splitting each row into a list.
If the list len was greater than the expected number of collumns (6), I concatonated the second and third elements because that's where the comma problem always was.

*UPDATE*
Thanks to piazza, now I know what's going on!

**UPDATE**
I DONE DID IT 

'''


SATdata = open('data_SAT2014.csv','r')
html = open('statsSAT.html', 'w')

#gets it started                                                                
tablehtml = '''
<!DOCTYPE html> 
<html>
<body style="color:white;background: black;">
<center>
<head><h1> 2014 New York SAT data </h1></head>
<p>This is a record of the SAT data from high schools in NYC.  High schools with less than 4 persons taking the test were omitted from this list.</p>
<table border="1px">
'''

data = SATdata.readlines()

#handles first collumn titles
firstrow = data[0].strip(' ,"\n\r') #gets rid of annoying commas in the beginnning and end
firstrow = ['School Code'] + firstrow.split(',')
for title in firstrow:
    tablehtml += '<th> '+ title +' </th>'
tablehtml += '\n'

#tableifies the rest 
nums = [[],[],[],[]]
for row in data[1:]:
    row = row.strip(' ,"\n\r')
    row = row.split(',')
    #fixes problems caused by commas in school names
    while len(row) > 6:
        row[1] = row[1] + ',' + row[2]
        del row[2]
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
        
#median stuff
def medianFind(nums):
    medians = []
    for block in nums:
        block.sort()
        if len(block) % 2 == 0:
            medians += [block[len(block)/2]]
        else:
            medians += [(block[len(block)/2] + nums[pos][(len(block)/2) + 1])/2]
    return medians
medians = medianFind(nums)
#adds median html
tablehtml +=  '\n\t<tr><td></td>\n\t<th>medians</th>'
for med in medians:
    tablehtml += '\n\t<td>' + str(med) + '</td>'
tablehtml += '\n\t</tr>'

#mean stuff
def meanFind(nums):
    means = []
    for block in nums:
        tot = 0
        for num in block:
            tot += num
        means += [tot/len(block)]
    return means
means = meanFind(nums)
#adds mean html
tablehtml +=  '\n\t<tr><td></td>\n\t<th>means</th>'
for mea in means:
    tablehtml += '\n\t<td>' + str(mea) + '</td>'
tablehtml += '\n\t</tr>'

#closes rest of tags 
tablehtml += '''
</table>
</center>
</body>
</html>
'''

#writes and closes files                                                        
html.write(tablehtml)
SATdata.close()
html.close()
