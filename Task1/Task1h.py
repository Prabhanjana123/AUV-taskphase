# Write a program that checks if the inputted number is a special number 
# (ex: palindrome, Armstrong number, perfect number etc).

num =  int(input("enter the number "))

##  for   palindrom  check 

temp = num  
reversed = 0 
while(temp>0):
    re =  temp%10 
    reversed =  reversed*10  +  re  
    temp =  temp//10 

if(reversed==num):
    print("number  is  a  plaindrome ")
else:
    print("number  is  a not  plaindrome ")

 ##    Armstrong number

temp  = num 

sum =  0 
count =0 

while(temp>0):
    count  =  count +1  
    temp =  temp//10

temp = num

while(temp>0):
    re =  temp%10 
    sum  =  sum  +  re**count   
    temp =  temp//10 

if(sum==num):
    print("number  is  a    Armstrong number ")
else:
    print("number  is  a not  Armstrong number ")
##   perfect number

sum =0 

for i in range(1,num):
    if(num%i==0):
        sum = sum + i 

if(sum==num):
    print("it is a  perfect number")

else:
    print("number  is  a not perfect number")