#8. Write a program to create a duplicate of an existing list. It should not point to same list.

li = [1,2,3,4,5,6]
new_list = []

for i in li:
    new_list.append(i)
print(new_list)
