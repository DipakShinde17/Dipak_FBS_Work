#4.Python Program to Find the Second Largest Number in a List Using Bubble Sort

def secondLargest(li):
    for i in range(len(li)):
        for j in range(0,len(li)-i-1):
            if(li[j] < li[j+1]):
                li[j],li[j+1] = li[j+1],li[j]
                print(li)
    
    for j in range(0,len(li)):
        if (li[i] != li[0]):
            return li[i]
        return -1

li = [10,20,30,40,50]
res = secondLargest(li)
print(res)
        
