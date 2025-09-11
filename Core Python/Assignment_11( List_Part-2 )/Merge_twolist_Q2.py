#2. Python Program to Merge Two Lists and Sort it

li1 = [2,1,3,5,4]
li2 = [33,11,33,66,55]

merge_list = li1 + li2
print("before sort :",merge_list)

for i in range(len(merge_list)):
    for j in range(0,len(merge_list) - i - 1):
        if(merge_list[j] > merge_list[j+1]):
            merge_list[j],merge_list[j+1] = merge_list[j+1],merge_list[j]
print("after sort:",merge_list)

