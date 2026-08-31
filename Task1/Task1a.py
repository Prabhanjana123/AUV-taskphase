#Write a program that checks if the inputted year is a leap year.

##  logic  is  if  the  number  ends  with  00   then   %  with  400   should  be  0   else  if  
#   it  doesnot  end  with 00   then   %4   should  be  0 

num =  int(input("enter  the number "))

temp =  num 
count = 0 
flag = 0 
while temp> 0:
    re =  temp%10  
    if(re!=0):
        flag  =1  
        break
    count=  count+1 
    if(count==2):
        break 
    temp =  temp//10
if(flag ==1 ):
    if(num%4==0):
        print("the  given  year  is  a leap  year ")
    else:
        print("the given  year  is  not a leap  year ")

else:
    if(num%400==0):
        print("the  given  year  is  a leap  year ")
    else:
        print("the given  year  is  not a leap  year ")



