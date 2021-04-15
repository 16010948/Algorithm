def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())

for i in range(t):
    n = int(input())
    half = n // 2
    for j in range(n // 2):
        if is_prime(half - j) and is_prime(half + j):
            print(half - j, half + j)
            break