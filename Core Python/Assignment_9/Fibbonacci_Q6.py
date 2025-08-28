#6. Write a program to print Fibonacci series using recursion.

def fibbo(num,a,b):
    if(num>0):
        c=a+b
        print(c)
        fibbo(num,a,b)
num=int(input("Enter number:"))
a=1
b=-1
fibbo(num,a,b)