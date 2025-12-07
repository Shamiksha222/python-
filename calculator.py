def add (x,y):
    return x + y 
def subtract (x,y):
    return x - y
def multiply (x,y):
    return x*y
def divide (x,y):
    return x/y

num1 = int(input("enter value 1:"))
num2 = int(input("enter value 2:"))
print("addition of two numbers is:" , add (num1,num2))
print("substraction of two numbers is:", subtract(num1,num2))
print("muliplication of two numbers is:", multiply(num1,num2))
print("division of two numbers is :", divide(num1,num2))