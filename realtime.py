import socket
from debuger import *
from guppy import hpy

h = hpy()

#read one line from the socket
def buffered_readLine(socket):
    buffer = ""
    while True:
        part = socket.recv(1)
        if part:
            buffer+=part

            if part == "\n":
                return buffer
        else:
            return None

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('0.0.0.0', 5555))
    serversocket.listen(5)

    listen()

    msgs = []
    try:
        while True:
            connection, addres = serversocket.accept()
            while True:
                got = buffered_readLine(connection)
                if got:
                    msgs.append(got)
                    print (msgs[-1])
                else:
                    break

    except IOError as e:
        "passed"
        pass
    except KeyboardInterrupt as e:
        print "here"
        print e
        connection.close()
        serversocket.close()
    except Exception as e:
        raise e

def print_heap(signum, frame):
    print h.heap()

if __name__ == '__main__':
    signal.signal(signal.SIGUSR2, print_heap)  # Register for remote debugging.
    main()