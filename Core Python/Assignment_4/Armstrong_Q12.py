#12. WAP to print Armstrong number within a given range.

num=int(input("Enter number : "))
temp=num
sum=0

while(temp>0):
    d=temp % 10
    temp=temp // 10
    sum=sum+d**3

if(sum==num):
        print("this number is armstrong number")
else:
        print("sorry but this number is not armstrong number ")
