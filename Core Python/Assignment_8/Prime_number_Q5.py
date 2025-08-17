def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
sum_primes = 0

for i in range(1, n + 1):
    if is_prime(i):
        sum_primes += i

print("Sum of all prime numbers between 1 and", n, "is:", sum_primes)
