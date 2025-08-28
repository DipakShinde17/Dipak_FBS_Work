#8. Write a program to create a duplicate of an existing list. It should not point to same list.

li = [1,2,3,4,5,6]
new_list = []

new_list.append(li)
print(id(new_list))
print("new list is :",new_list)
print(id(li))