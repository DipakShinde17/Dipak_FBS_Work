#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

sideA=int(input("Enter a side:"))
sideB=int(input("Enter b side:"))
sideC=int(input("Enter c side:"))

if( sideA == sideB and  sideB == sideC):
    print(" Equilater")


elif( sideA == sideB or  sideB == sideC or  sideA == sideC):
    print("isosceles")

elif( sideA != sideB and sideB != sideC):
    print("scalene")

else:
    print("......")