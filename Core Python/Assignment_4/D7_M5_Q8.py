#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.

num=int(input("Enter number :"))
i=1

while(i<=num):
    if(num%7==0):
        print("this number is divisiable by 7")
    elif(num%5==0):
        print("this number is divisiable by 5")
    else:
        print("this number is not divisiable 7 and 5")
    break


