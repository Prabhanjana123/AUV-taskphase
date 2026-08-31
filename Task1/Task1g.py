# Write a function to check if a string is a palindrome or not.

import sys 

def pal():
    str =  input("enter  the  string ")

    size =  len(str)

    for i in range(size//2):
     if(str[i]!=str[size-i-1]):
            print("not  a palindrome ")
            sys.exit()

    print("it is  a palindrome ")

pal()