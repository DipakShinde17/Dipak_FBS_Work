#11. WAP to check if a given number is Armstrong number or not. Foreach task create separate functions.

def arm():
    n=int(input("Enter a number : "))
    temp=n
    sum=0
  
    d1=temp % 10
    temp= temp // 10
    sum=sum+d1**3
    
    if(sum==n):
        print("not armstrong")
    else:
        print("armstrong")

arm()