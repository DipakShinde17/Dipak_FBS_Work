li = [10,11,12,13,14,15]
max = li[0]
smax = 0
for i in range(1,len(li)):
    if(li[i] > max):
        smax = max
        max=li[i]
    
    if(li[i] < smax):
        smax = li[i]
print("second largest number:",smax)
print("first largest number:",max)

