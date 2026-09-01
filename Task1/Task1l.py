# Write a program with functions to implement Linear and Binary search

def binary():
    arr= [1,2,3,4,5,6,7,8]
    num =  int(input("enter  the number to find "))
    l= 0  
    r = len(arr) - 1 
    while(r>=l):
        mid = (r+l)//2  
        if(arr[mid]>num):
            r =  mid-1 
        elif (arr[mid]<num):
            l = mid+1 
        else:
            print("number found  at index  in  binary ",mid)
            return

    print("number not found")

def linear():
    arr= [1,2,3,4,5,6,7,8]
    num =  int(input("enter  the number to find "))
    for i  in range(len(arr)):
        if(arr[i]==num):
            print("number found  at index  in linear",i)
            return            
    print("number not found") 


binary()

linear()