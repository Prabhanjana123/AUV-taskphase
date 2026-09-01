# A college printer receives print requests from students. The requests 
# must be processed in the same order in which they were received. 
# Implement the concept of queues to simulate the printer queue.

from collections import deque
queue= deque()

def printerinput():
    num =  int(input("enter  the page  number  to print "))
    queue.append(num)

def printeroutput():
    while(len(queue)!=0):
        print("printed page number :  ",queue.popleft())
        

printerinput()
printerinput()
printerinput()
printeroutput()