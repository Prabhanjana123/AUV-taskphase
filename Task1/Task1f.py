# Write a program that counts the number of appearances of each letter in 
# a string and prints it out as a dictionary.

str =   input(" enter  the  string  :  ")

dic ={}
for l  in str :
  dic[l] =  dic.get(l,0)+1  ##    here   get  finds  if dic[l]  is   there  else  makes  default  value  as 0 
  

print(dic)