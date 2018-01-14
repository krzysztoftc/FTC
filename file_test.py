#
#def open_file(file):
#	print "opening file:", file
#	f = open(file)
#	# open_file('dummy.txt')
def give_me_leak():
	f = open('dummy.txt')
	return f

def main():
	for i in range(0,100):
		give_me_leak()
	while 7:
		pass
	# f.close()

main()
#try:
#	while 6:
#		pass
#except Exception as e:
#	print e
#	pass
