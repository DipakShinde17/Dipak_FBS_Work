'''Write a program to find sum of following series using recursive functions:
i. 1! + 2! + 3! + 4! +..... + n!
Note : For fact and sum two recursive functions'''

def fact(num):
    if(num==0):
        return 1
    else:
        return num*fact(num-1)
    
def sum(num):
    if(num==0):
        return 0
    else:
        return fact(num) + sum(num-1)
    
num=int(input("Enter number :"))
res=sum(num)
print("sum of series:",res)
