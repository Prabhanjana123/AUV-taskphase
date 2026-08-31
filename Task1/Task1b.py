#Write a program that prints every prime number between 1 and n

import  sys  ##   used  to  exit   from  code 

n = int(input("enter  the  number n "))

if(n<=1):
    print("no    prime  numbers  present ")
    sys.exit()

for i in  range(2,n+1):
    flag =0 
    for j  in range(2,int((i/2))+1):
        if(i%j==0):
            flag =1 
            break
    if(flag==0):
        print(i)
            