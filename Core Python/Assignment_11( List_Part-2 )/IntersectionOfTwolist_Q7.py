#7. Python Program to Find the Intersection of Two Lists
li1 = [1,2,3,4,5]
li2 = [1,6,7,8,4]

intersection = []

for i in li1:
    if(i in li2 and i not in intersection):
        intersection.append(i)
print(intersection)