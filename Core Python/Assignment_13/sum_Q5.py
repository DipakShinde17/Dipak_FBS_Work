#5. Python Program to Sum All the Items in a Dictionary

dict1 = {1:101,2:102,3:103,4:104,}
sum1 = 0
sum = 0
for i in dict1.values():
    sum = i + sum


for j in dict1.keys():
    sum1 = sum1 + j


sum_of_all_items = sum1 + sum
print("sum of all items ",sum_of_all_items)