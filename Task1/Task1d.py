# Given a list of numbers, create functions that return largest and smallest 
# numbers in the list (without using max() or min()).
arr =[1,2,3,4,5,6,7]

def maximum():
    maxi=  arr[0] 
    for i in arr:
        if(i>maxi):
            maxi = i

    return maxi

def minimum():
    mini=  arr[0] 
    for i in arr:
        if(i<mini):
            mini = i

    return mini

print(maximum())
print(minimum())