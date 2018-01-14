from guppy import hpy
import time
import datetime
import sys
import numpy
from debuger import listen
import array, itertools
h = hpy()
import guppy.heapy.RM
ll = []
l = [0]
def do_sth():
    global h
    # logs = open('heap.log','w+')
    #print h.heap()
    # logs.write("\nFunc do_sth()\n")
    # logs.write (str(h.heap()))
    a = l[-1]
    print l
    # logs.write("\nAfter do_sth()\n")
    # logs.write (str(h.heap()))

    ll.append(array.array('B', itertools.repeat(0, 10000)))
    return a+1

def main():
    listen()
    # logs = open('heap.log', 'w')

    while True:
        l.append(do_sth())
        print sys.getsizeof(ll)
        time.sleep(0.1)

main()
