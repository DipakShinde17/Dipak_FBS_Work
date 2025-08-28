#7. Write a program to find sum of digits using recursion.

def sum_of_digite(num):
    if(num==0):
        return 0
    else:
        return num%10 +sum_of_digite(num // 10)
    
n=int(input("Enter number: "))
res=sum_of_digite(n)
print(f"{n} sum of digite is : {res}")

