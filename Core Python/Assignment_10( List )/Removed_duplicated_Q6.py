#6. Write a program to remove duplicates from the list.

li=[11,23,45,11,80]
new_li=[]

for i in li:
    if  i not in new_li:
        new_li.append(i)
print(new_li)