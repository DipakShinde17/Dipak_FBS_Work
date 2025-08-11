#11. WAP to check if given number Strong Number.
''' A number is called strong number if sum of the factorial of its digit is equal to 
number  itself.'''

num = int(input("Enter number :"))
temp=num
sum=0

while(temp>0):
    d=temp%10
    temp=temp//10
   
    i=1
    fact=1
    while(d>=i):
        fact=fact*i
        i=i+1
    sum=fact+sum
if(sum==num):
        print("strong")
else:
        print("not strong")
        

