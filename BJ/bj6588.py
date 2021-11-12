import sys
input = sys.stdin.readline
MAX = 1000000

is_prime = [True] * (MAX + 1)
odd_primes = []
for i in range(2, int(MAX ** 0.5) + 1):
    for j in range(i * i, MAX + 1, i):
        is_prime[j] = False

for i in range(2, MAX + 1):
    if i % 2 == 1 and is_prime[i]:
        odd_primes.append(i)

while True:
    n = int(input())

    if n == 0:
        break

    for odd_prime in odd_primes:
        if is_prime[n - odd_prime]:
            print(n, "=", odd_prime, "+", (n - odd_prime))
            break