#Program to Find the Roots of a Quadratic Equation
A=int(input("Enter value of a :"))
B=int(input("Enter value of b :"))
C=int(input("Enter value of c :"))

sqrt=((B**2) - (4*A*B*C)) **0.5

Res1=(-B+sqrt) / 2 * A
Res2=(-B-sqrt) / 2 * A

print(f"Quadratic Equation:{Res1} {Res2}")