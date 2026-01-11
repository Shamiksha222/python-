file = open('Codingal.txt','r')
file2 = open('Codingalupdated.txt','w')

a = file.readlines()
type(a)
for i in range(1, len(a)+1):
    if(i%2 !=0):
        file2.write(a[i-1])
    else:
        pass

file2.close()
file2 = open('Codingalupdated.txt', 'r')

b = file2.read()

print(b)

file.close()
file2.close()