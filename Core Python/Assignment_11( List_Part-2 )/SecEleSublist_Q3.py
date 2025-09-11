#3. Python Program to Sort the List According to the Second Element in Sublist

li = [[1,5],[3,1],[5,2],[2,7]]

for i in range(len(li)):
    for j in range(0,len(li) - i - 1):
        if(li[j] > li[j+1]):
            li[j],li[j+1] = li[j],li[j+1]
print(li)