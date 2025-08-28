#13 . Write a program to print list after removing even numbers.

li = [1,2,3,4,5,6,7,8]
odd_li = []

for i in li:
    if(i % 2 == 1):
        odd_li.append(i)
print("removing even number list is :",odd_li)