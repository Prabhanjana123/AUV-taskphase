# Write a function that calculates factorial of a given number using 
# regression and memoization.

def function(n):
    if(n<=1):
        return 1 
    else:
         return n*function(n-1)

n =  int(input("enter  the  number to  find factorial  by  recursion "))
print(function(n))



def memo(n,arr):
      if(n<=1):
           return 1 
      elif(arr[n]!=-1):
           return arr[n]
      else:
           arr[n] = n*memo(n-1,arr)
           return arr[n]
n =  int(input("enter the number to   find  factorial  by   memoization"))
arr = [-1]*(n+1) 
print(memo(n,arr))      
           

