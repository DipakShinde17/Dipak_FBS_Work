#Find the sum of three-digit number.

digit=int(input("Enter three digit"))
temp=digit

d1= temp % 10
temp= temp // 10 

d2= temp % 10
temp= temp // 10

d3= temp % 10
temp = digit // 10

sum= d1+d2+d3

print(f"d1 : {d1} d2 : {d2} d3 : {d3}")
print(sum)
