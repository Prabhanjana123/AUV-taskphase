# Write a program with functions to implement Bubble sort, Insertion Sort, 
# Selections sort.

arr =  [1,9,2,8,3,7]
size =  len(arr)

def bubble():
    arr =  [1,9,2,8,3,7] 
    for i  in range(size):
        for j in range(size-i-1):
            if(arr[j]>arr[j+1]):
                temp =  arr[j]
                arr[j] = arr[j+1] 
                arr[j+1] = temp 

    print("arr  after bubble  sorting :  ",arr)



def sel():
    arr =  [1,9,2,8,3,7] 
    for i  in range(size):
        min = i
        for j in range(i+1 ,size):
            if(arr[j]<arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp 

    print("arr  after  selection sorting ",arr)

def inser():
    arr =  [1,9,2,8,3,7] 
    for i   in range(size):
        key =  arr[i]
        j = i-1 
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j= j-1  

        arr[j+1] = key 
    print("arr  after  insertion sorting ",arr)


inser()

bubble()

sel()    