def factorial(num, x):
    total = 1
    for i in range(x):
        total *= (num - i)
    return total

n, k = map(int, input().split())
print((factorial(n, k) // factorial(k, k)) % 10007)