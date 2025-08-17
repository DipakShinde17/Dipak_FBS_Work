def pailindrome():
    number=int(input("Enter a number : "))
    temp=number
    
    d1=temp // 100
    temp = temp % 100

    d2= temp // 10
    temp = temp % 10

    d3= temp // 1
    temp = temp % 1

    rever_num= (d3*100)+(d2*10)+d1
    print("revers number : ",rever_num)

    if(rever_num==number):
        print("number is pailindrom")
    else:
        print("number is not pailindrom")
pailindrome()