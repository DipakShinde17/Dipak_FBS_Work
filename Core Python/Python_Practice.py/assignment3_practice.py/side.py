side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))



if((side1+side2)>side3 or (side2+side3)>side1 or (side1+side3)>side2):
    print("traingle is correct")

else:
    print("traingle is uncorrect")
    