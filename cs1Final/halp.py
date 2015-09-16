def main():
	#initiation
	start = raw_input('Do you want to create a html file? (y/n): ')
	while start != 'n':
		if start == None:
			return 'File aborted'		
		elif start == 'y':	#start function
			#stuff
			print 'starting'
		else:
			print 'bad input, try again'
			start = raw_input('Do you want to create a html file? (y/n): ')
	elif start == 'n':
		return 'closing'
