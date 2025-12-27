#number chose by judge
n = 25

print("Welcome to the coding competition!")


while True:
    guess= int(input("Enter your guess:"))

    if guess > n :
        print("your guess is higher then the correct value")
    elif guess < n :
        print("your number is lower than the correct value")
    else:
        print("You got the correct ans!")
       
    