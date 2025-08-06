p=int(input("Enter p value="))
t=int(input("Enter t value="))
r=int(input("Enter r value="))

cal=p*(1 + r / 100)**t-p

print(f"principle={p}\n rate={r}\ntime={t}")
print(f"compound interest={cal}")

