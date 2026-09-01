# Write a program that simulates a basic calculator: it should ask the user 
# for two numbers and an operator (+, -, *, /), then print the result. Handle 
# division by zero using try/except

num1 =  int(input("enter  number 1 "))
num2 =  int(input("enter  number 2 "))
ope =   (input("enter thw  operator "))

match ope:
    case '+' :
        print(num1+num2)
    case '-' :
        print(num1-num2)
    case '*' :
        print(num1*num2)
    case '/' :
        try:
            print(num1/num2)
        except:
            print("num2 cannot  be 0 ")
    case _: print("unknown  operator ")

        
