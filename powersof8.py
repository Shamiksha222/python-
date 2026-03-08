def power8(number):
    if number <=0:
        return False
    return (number &(number-1)==0 and (number -1) % 7 == 0)

number = int(input("enter your number:"))

if (power8(number)):
    print("\nThe number is a power of 8")
else:
    print("\nThe number is not a power of 8")