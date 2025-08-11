#10.Perfect Number

num = int(input("Enter number :"))
temp=num
sum=0

while(temp>0):
    d=temp % 10
    temp= temp // 10

    