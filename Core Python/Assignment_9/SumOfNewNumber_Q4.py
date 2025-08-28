#4. Write a program to find sum of n numbers using recursion.

def sum_of_number(num):
    if(num==0):
        return 0
    else:
        return num+sum_of_number(num-1)
num=int(input("Enter number :"))
res=sum_of_number(num)
print(res)