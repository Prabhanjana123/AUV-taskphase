# Implement a Stack from scratch; write functions for pop, push and 
# display.

stack= []

def pop():
    if(len(stack)==0):
        print("nothing to  return ")
    else:
        print("returned : ",stack[-1])
        stack.pop()

def push():
    num = int(input("enter  the  number : "))
    stack.append(num)
    print("ADDED  number ")

def display():
    print("the   stack is ",stack)

push()
push()
pop()
display()