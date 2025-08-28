#2. Write a program to check if given number is Armstrong or not using recursive function.

def armstrongNo (num):
    temp = num
    digit = len(str(num))
    sum =0
    while temp > 0:
        d = temp % 10
        sum += d**digit
        temp=temp//10
    print(sum)
    return sum

num = int(input("Enter Number = "))
result = armstrongNo(num)

if num == result:
    print("Number is Armstong.")
else:
    print("Number is not Armstrong.")
    
    