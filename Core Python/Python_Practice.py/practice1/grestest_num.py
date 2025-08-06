num1=int(input("Enter 1st number :"))
num2=int(input("Enter 2nd number :"))
num3=int(input("Enter  3rd number")) 

if(num1>num2):
    if(num1>num3):
       print("number1 is greater")
       if(num2>num3):
           print("num2 is greater")
       else:
           print("number is 2 is less")
    else:
        print("number 2 is less")
else:
    print("number 3 is less")
