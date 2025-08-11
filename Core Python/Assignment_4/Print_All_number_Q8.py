#9. WAP to print all numbers in a range divisible by a given number.
divisor=int(input("Enter number :"))
for num in range(10,50+1):
    if num % divisor == 0:
        print(num,end=" ")