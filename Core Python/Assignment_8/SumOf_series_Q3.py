#3. Write a program to find sum of following series using functions :
'''a. 1+ 2 + 3 + 4+..... + n
b. 1!+ 2! + 3! + 4!+..... + n!
c. 1^1 + 2^2 + 3^3+ ...... n^n'''

def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

n=int(input("Enter number(sum): "))
res=sum_of_series(n)
print(f"sum of series {res}")

n=int(input("Enter number(sum): "))
res=factorial(n)
print(f" factorial is {res}")


    
