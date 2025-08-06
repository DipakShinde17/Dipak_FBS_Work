num= int(input("Enter three digits number : ")) #428
d1=num//100
d=num//10
d2=d%10
d3=num%10
print(f"D1 {d1} D2 {d2} D3 {d3}")




if (d1/2==d2 and d3/2==d1):
    print("yes you have done it")
else:
    print("pleas next time")

