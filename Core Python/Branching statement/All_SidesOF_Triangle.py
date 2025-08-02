A=int(input("Enter AB value"))
B=int(input("Enter BC value"))
C=int(input("Enter AC value"))


if(A+B)>C and (B+C)>A and (A+B)>B:
    print("valid")

else:
    print("Unvalid")
    
