#6. Write a program to find print the following Fibonacci series using


num=int(input("Enter number : "))
a=0
b=1
for i in range(0,num+1):
    c=a+b
    a=b
    b=c
    print(c)