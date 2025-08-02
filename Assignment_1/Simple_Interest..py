#Write a program to enter P, T, R and calculate simple Interest.

P=int(input("Enter principal value: "))
R=int(input("Enter internal rate : "))
T=int(input("Enter time in year : "))

SL= P*T*R/100

print(f"simple interst is {SL} ")