#Write a program to input angles of a triangle and check whether triangle is valid or not.


A=int(input("enter A value:-"))
B=int(input("enter B value:-"))
C=int(input("enter C value:-"))

if(A+B+C==180):
    print("traingle is valid")

else:
    print("traingle is invalid")