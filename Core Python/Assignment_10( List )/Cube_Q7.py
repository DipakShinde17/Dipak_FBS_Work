#7. Write a program to create a new list from existing list which contains cube of
#each number of list.

li = [1,2,3,4,5]
new_list = []

for i in li:
    cube=i**3
    new_list.append(cube)
print(new_list)