#3. Write a program to reverse a given number using recursive function.

def revers(num,rev=0):
    if(num==0):
        return rev
    else:
        return revers(num // 10,rev*10+num % 10)
    
num=int(input("Enter number : "))
res=revers(num,rev=0)
print(res)
