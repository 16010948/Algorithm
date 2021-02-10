import math
n = int(input())
m = int(input())
prime = [True] * (m + 1)

prime[0] = False
prime[1] = False

for i in range(2, int(math.sqrt(m)) + 1):
    for j in range(i + 1, m + 1):
        if not prime[j]:
            continue
        if j % i == 0:
            prime[j] = False

min_prime = m
sum_primes = 0
for i in range(n, m + 1):
    if prime[i]:
        min_prime = min(min_prime, i)
        sum_primes += i

if sum_primes == 0:
    print(-1)
else:
    print(sum_primes)
    print(min_prime)
