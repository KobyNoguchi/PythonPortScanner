# PORT SCANNING IS ILLEGAL WITHOUT CONSENT
# if a connection succeeds, prints this port is open 

import socket
import threading
from queue import Queue

target = '127.0.0.1' # use your own ip or localhost 127.0.0.1
queue = Queue()

open_ports = [0]

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        #we are saying connect to the target on this particular port
        return True
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print("Port {} is open!".format(port))
            open_ports.append(port)
        

port_list = range(1, 5000)
fill_queue(port_list)
thread_list = []

for t in range(100):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("Open ports are: ", open_ports)





"""
#Very inefficient very slow, no threading
for port in range(1, 1024):
    result = portscan(port)
    if result: 
        print("Port {} is open!".format(port))
    else:
        print("Port {} is closed!".format(port))


"""