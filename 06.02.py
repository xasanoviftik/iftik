import copy 

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1 = list2

print(id(list1))
print(id(list2))

list3 = [1, 2, 3]

list4 = copy.deepcopy(list3)

print(id(list3))
print(id(list4))