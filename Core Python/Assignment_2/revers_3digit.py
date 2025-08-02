#Write a program to reverse three-digit number.
Revers=int(input("Enter value"))
temp=Revers

a= temp // 100
temp = temp % 100

b= temp // 10
temp = temp %10

c= temp // 1
temp = temp % 1

revers_num= (c*100)+(b*10)+a
print(f"revers number is : {revers_num}")