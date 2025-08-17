#8. Write a program find reverse of a number

def rever():
    n=int(input("Enter number : "))
    temp=n
    
    d1= temp // 100
    temp= temp % 100

    d2= temp // 10
    temp = temp %10

    d3= temp // 1
    temp = temp % 1

    reves_num= (d3*100) + (d2*10)+d1
    print(f"revers number is {reves_num}")
rever()