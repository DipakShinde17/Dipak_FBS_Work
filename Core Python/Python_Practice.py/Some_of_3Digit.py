digit=int(input("Enter digit: "))
temp=digit

a=temp % 10
temp= temp // 10

b= temp % 10
temp = temp // 10

c= temp % 10
temp = temp // 10

sum= a+b+c

#print(f"total of three digit A :{a} B: {b} C: {c}")
print(sum)