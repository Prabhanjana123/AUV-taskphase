# Given a string, write a program that does simple string operations and 
# prints. (ex: upper(), lower(), title(), split(), etc).

str =  input("enter the  string ")

c =  int(input("enter  1  for upper() ,  2 for  lower() , 3 for title() , 4 for  split()"))

match c :
    case 1 : print(str.upper())
    case 2 : print(str.lower())
    case 3 : print(str.title())
    case 4 : print(str.split())
    case _ : print("invalid input ")

