import gc


counter = 0
counter2 = 0
list_of_msg = []

#@profile
def main():
	# gc.disable()
	print "GC is " + "enable" if gc.isenabled() else "disabled"
	global list_of_msg
	
	for i in range (1,100000000):
		new_msg()
		#read_msg()
	end()
	print list_of_msg
	list_of_msg = None
	end() 

def end():
	print "counter is: ", counter

#@profile
def new_msg():
	global counter
	global counter2
	global list_of_msg
	list_of_msg.append('meassage'*1000 + str(counter2))
	print "added object no", counter2
	counter += 1
	counter2 += 1

def read_msg():
	global counter
	global list_of_msg
	while counter:
		print list_of_msg[-counter]
		counter -= 1

if __name__ == '__main__':
	main()
