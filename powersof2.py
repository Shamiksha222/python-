def power2(number):
    if number <=0:
        return False
    return (number &(number-1)==0)

number = int(input("enter your number:"))

if (power2(number)):
    print("\nThe number is a power of 2")
else:
    print("\nThe number is not a power of 2")