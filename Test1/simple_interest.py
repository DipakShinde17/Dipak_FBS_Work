#2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100)

p=int(input("enter p :"))
r=int(input("enter r :"))
t=int(input("enter t :"))

S_I=(p*t*r)/100

print(f"simple interst : {S_I}")