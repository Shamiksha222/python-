lst = [1,2,3,4,5]

print("length of list:", len(lst))
print("the first element:", lst(0))
print("the last element:", lst(-3))
lst.append(6)
print("the updated list is:", lst)


lst.remove(2)
print("the updated list is:", lst)

lst.pop(4)
print("the updated list is:", lst)

lst.sort()
print("the updated list is:", lst)


lst.reverse()
print("the updated list is:", lst)

lst = lst[1:4:1]
print("the updated list is:", lst)

lst.clear()
print("the updated list is:", lst)