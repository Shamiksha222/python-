#empty tuple
my_tuple=()
print(my_tuple)

#tuple having integers
my_tuple = (1,2,3)
print(my_tuple)

#tuple with mixed data types
my_tuple = (1,"hello", 4.5)
print(my_tuple)

#nested tuple
my_tuple = ("mouse", [8,4,6], (1,2,3))
print(my_tuple)

#accessing tuple elements using indexing
my_tuple = ("p", "g", "f", "q", "t")
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[4])

#nested tuple
print("nested tuple")
n_tuple = ("bunny","cat" ,[1,2,3,4])
print(my_tuple)

#nested index
print("nested index")
print(n_tuple[2][3])
print(n_tuple[1][0])

#slicing
print("slicing")
print("sliced:", my_tuple[1:3])

#iteration
for letter in (my_tuple) :
    print("hello", letter)
