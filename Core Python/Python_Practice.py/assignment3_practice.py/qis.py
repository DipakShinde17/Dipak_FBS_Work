sideA=int(input("Enter sideA="))
sideB=int(input("Enter sideB="))
sideC=int(input("Enter sideC="))

if(sideA==sideB==sideC):
    print("equilater")
elif(sideA==sideB or sideC==sideA or sideB==sideC ):
    print("isosceles")
else:
    print("scalene")