#python program to create a simple calculator 

# 3step to build calculator progrM
# functions for operations 
#user input 
#print result 

#step-1 create 
#functions to add two numbers 
def add(num1,num2):
    return num1 + num2 

#functions to addsubstract two numbers 
def sub(num1,num2):
    return num1 + num2 

#functions to multiply two numbers 
def multiply(num1,num2):
    return num1 + num2 

#functions to divide two numbers 
def divide(num1,num2):
    return num1 + num2 

#functions to  multiply two numbers 
def avg(num1,num2):
    return (num1 + num2)/2  

#step-2: user input 
print ( "please select a operation :\n " \
       "1. Addition\n" \
       "2. Substraction\n"
       "3. Multiplication\n" \
       "4. Division\n" \
       "5. Average\n"  )

select = int(input("select a operation from 1,2,3,4,5: ")) 
number1= int(input("enter first number: "))
number2= int(input("enter second  number: "))

# step-3: print the result 

if select == 1:
    print(number1, "+", number2, "=", \
            add(number1 , number2 ))
    

elif select == 2:
    print(number1, "-", number2, "=", \
            sub(number1 , number2 ))
    

elif select == 3:
    print(number1, "*", number2, "=", \
            multiply(number1 , number2 ))
    
    
elif select == 4:
    print(number1, "/", number2, "=", \
            divide(number1 , number2 ))
    

elif select ==5:
    print("(",number1, "+", number2,")", "/", "2", "=", \
            avg(number1 , number2 ))
    
else:
    print("invalid operation! pls select again!")
