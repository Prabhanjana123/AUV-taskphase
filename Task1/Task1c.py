#Write a program to let the user input a list and search for an element.

import sys 
num =  int(input("enter  the  number of elements :  "))

arr =[]

for i in range (num):
    temp =  int(input("enter  the  numnber  "))
    arr.append(temp)

target =  int(input("enter  the  number  to  find "))

for i in range (num):
    if(arr[i]==target):
        print("elemet found ")
        sys.exit()

print("element  not  found ")
        