import sys
from memory_profiler import profile

def func_with_class(i):
	class Foo():
		def __init__(self, i):
			self.g = i
		def func_foo(self):
			self.g += 1
		def func_foo2(self):
			self.g += 1
			print g	
	
	m = Foo(i)
	return m

@profile(precision=8)
def main():
	l = [] 
        for i in range(0,100000):
		# func_with_class(i+7).func_foo()
		l.append(func_with_class(i+7))
	for j in l:
		j.func_foo()
	print "type", type(l[0]),sys.getsizeof(l[0])  
	print "type", type(l[-1]),sys.getsizeof(l[-1])  
	l = []
	print

@profile
def run():
	main()
	#print "wait for ctrl+c"
	#try:	
	#	while 666:
	#		pass
	#except:
	#	return 0

if __name__ == '__main__':
	run()

