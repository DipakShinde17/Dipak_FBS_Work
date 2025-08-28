#10. Write a program to remove all occurrences of a given element in the list.
li = [1,2,3,4,5]
num = int(input("Enter number to removed: "))
result = []
for i in li:
    if(i != num):
        result.append(i)

print(f"removed element {num} and updated list : {result}")


