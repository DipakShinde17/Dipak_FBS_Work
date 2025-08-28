#2. Write a program to find maximum and minimum element in a list.

li = [12,34,56,78,90]
max=li[0]
for i in range(1,len(li)):
    if(li[i] > max):
        max=li[i]
print("maximum number is :",max)

min=li[0]
for i in range(1,len(li)):
    if(li[i] < min):
        min = li[i]
print("minimum number is ",min)
