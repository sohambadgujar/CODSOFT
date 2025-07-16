# Task 2 : Calculator 

num1 = float(input("Enter the first numberL:    "))
num2 = float(input("Enter the second number:    "))

# User input 
print("Choose an operation:     ")
print(" Addition (+)")
print(" Substraction (-)")
print(" Multiplication (*)")
print(" Division (/)")
operation = input("Enter for your operation (+,-,*,/)   :   ")

# To perform the calculator 

if operation == '+':
    result = num1 + num2
    print(f" {num1} + {num2} = {result}")
    
elif operation == '-':
    result = num1 - num2
    print(f" {num1} - {num2} = {result}")
    
elif operation == '*':
    result = num1 * num2
    print(f" {num1} * {num2} = {result}")
    
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f" {num1} / {num2} = {result}")
    else:
        print("Error : Division by zero is not allowed")

else:
    print("Invalid operation. Please Enter only +,-,*,/")
    