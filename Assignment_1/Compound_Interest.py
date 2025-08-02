#Write a program to enter P, T, R and calculate Compound Interest.

P=int(input("Enter principle value :"))
T=int(input("Enter internal rate: "))
R=int(input("Enter year of time : "))

C_I= P*(1 + R / 100)**T-P

print(f"compound interest is {C_I}")