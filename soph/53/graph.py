def graph(d1,d2):
	top = max(max(d1),max(d2))
	s = ''
	while top > 0:
		col = 0
		while col < len(d1):                     
			if d1[col] >= top:                             
				s += '* '                     
			else:                             
				s += '  '
			if d2[col] >= top:
				s += '^  '
			else:	
				s += '   '             
			col += 1
		print s             
		s = ''             
		top -= 1     
	district = ['Q','X','K','R','M']
	for dis in district:
		s += dis + '    '             	
	print s     
	print '---' * len(d1+d2)
graph([3,4,5],[8,7,6])
