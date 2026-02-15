numberLargest = int(input("enter largest no."))
numberSmallest = int(input("enter smallest no."))
while(numberSmallest):
    a = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = a
print("HCF is: ", numberLargest)