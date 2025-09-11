#1. Python Program to Put Even and Odd elements of a List into two Different Lists

li = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even_li = []
odd_li = []


for i in li:
    if(i % 2 == 0):
        even_li.append(i)
    elif(i % 2 == 1):
        odd_li.append(i)


print("Even number list: ",even_li)
print("Odd number list : ",odd_li)
