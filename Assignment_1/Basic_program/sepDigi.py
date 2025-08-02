num = int(input("enter a three digit num : "))

temp = num #258

d1 = temp % 10
temp= temp//10

d2 = temp % 10
temp= temp//10

d3 = temp % 10
temp= temp//10

print(f'the seprate digit is d1 : {d1} , d2 : {d2},  d3 {d3}')