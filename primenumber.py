num = int(input("enter a number:"))
if num > 1:
    for i in range (2, int(num**0.5)+1):
        if (num % i == 0):
            print (num, "the given number is not an integer")

        else:
            print("the given number is a prime number")
else:
    print("the given number is not a prime number")
    
