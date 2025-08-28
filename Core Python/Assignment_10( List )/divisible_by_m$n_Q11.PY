#11. Write a program to print all numbers which are divisible by m and n in the list.

li = [10, 12, 15, 20, 24, 30, 36, 40, 45, 48, 50]
n = int(input("Enter number(n): "))
m = int(input("Enter number(m): "))

print(f"\nNumbers divisible by both {m} and {n} are:")

for i in li:
    if(i % n ==0 and i % m == 0):
        print(i)

