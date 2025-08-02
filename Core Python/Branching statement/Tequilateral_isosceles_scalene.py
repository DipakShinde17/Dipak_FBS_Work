A=int(input("Enter a side:"))
B=int(input("Enter b side:"))
C=int(input("Enter c side:"))

if( A==B & B==C):
    print(" Equilater")


elif(A==B or B==C):
    print("isosceles")

elif(A!=B & B!=C):
    print("scalene")

else:
    print("......")