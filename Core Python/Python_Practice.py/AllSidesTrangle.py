side1=int(input("Enter 1st side: "))
side2=int(input("Enter 2nd side: "))
side3=int(input("Enter 3rd side: "))

if((side1+side2) > side3 and (side1+side3) > side2 and (side2+side3) > side1):
    print("valied")
else:
    print("invalied")