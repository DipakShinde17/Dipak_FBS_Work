#WAP to calculate total salary of employee based on basic, da=10% of basic,ta=12% of basic, hra=15% of basic.

A=int(input("Enter Value:"))

TA= (A*12)/100
DA= (A*10)/100
HRA= (A*15)/100

print(f"TA : {TA} DA : {DA} HRA : {HRA} ")