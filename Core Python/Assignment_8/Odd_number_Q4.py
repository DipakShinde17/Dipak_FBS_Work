#Sum of all odd numbers between 1 to n

def odd():
    num=int(input("Enter number : "))

    for num in range(1,num+1):
        if(num%2==1):
            print(num)
odd()