import sys

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


input = sys.stdin.readline
n, m = map(int, input().split())

for x in range(n, m + 1):
    if is_prime(x):
        print(x)