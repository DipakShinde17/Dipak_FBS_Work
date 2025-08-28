#12. Write a program to create three lists of numbers, their squares and cubes

li = [1,2,3,4,5,6,7,8,9]
squre_li = []
cube_li = []

for i in li:
    cube = i**3
    squre = i**2
    cube_li.append(cube)
    squre_li.append(squre)
print("cube list is : ",cube_li)
print("squre list is :",squre_li)