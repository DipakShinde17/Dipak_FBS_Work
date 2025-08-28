def prime(num):
    for i in range(2,num//2 +1):
        if(num%i==0):
            return False
    else:
        return True
    
num=int(input("Enter number: "))
res=prime(num)
if(res):
    print("this number is prime")
else:
    print("this number is not a prime")

    
