#9. Write a program to create three lists of numbers, their squares and cubes

num = int(input("Enter element in list: "))
numbers = []
squres = []
cube = []

for i in range(1,num):
    numbers.append(i)
    squres.append(i ** 2)
    cube.append(i ** 3)

print("list is : ",numbers)
print("list squres:",squres)
print("list cube :",cube)
