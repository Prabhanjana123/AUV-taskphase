# Write a function that multiplies two user inputted matrices

import sys  

def func():
    r1 =  int(input("enter row1 "))
    c1 = int(input("enter col1 "))


    r2 =  int(input("enter row2 "))
    c2 = int(input("enter col2 "))

    if(c1!=r2):
        print("we cannot   these  two matrixes ")
        sys.exit() 
    print("enter  the elements of  mat1 ")
    mat1 = [[0]*c1 for _ in range(r1)]
    mat2 = [[0]*c2 for _ in range(r2)]


    for i in range(r1):
        for j in range(c1):
            mat1[i][j] = int(input("enter value "))
    

    print("enter  the elements of  mat2 ")

    for i in range(r2):
        for j in range(c2):
            mat2[i][j] = int(input("enter value "))

    mat3 = [[0]*c2 for _ in range(r1)] 

    for  i in range(r1):
        for j in range(c2):
                for k in range(c1):
                    mat3[i][j] =  mat3[i][j] + (mat1[i][k] * mat2[k][j]) 


    print("final matrix  is :  ")

    for  i in range(r1):
        for j in range(c2):
                print(mat3[i][j], end=" ")
        print("")
    

func()