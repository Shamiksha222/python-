def factorial(n):
    if n == 1:
        return n
    else :
        return n* factorial(n-1)
num =int(input("enter a number:"))
if num < 0 :
    print ("no negative numbers accepted")
elif num == 0 :
    print ("no zeros allowed")
else:
    print("Factorial of n is : " , factorial(num))