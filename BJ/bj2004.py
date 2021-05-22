import sys
input = sys.stdin.readline

def count_five(n):
    total = 0
    while n > 0:
        n //= 5
        total += n
    return total

def count_two(n):
    total = 0
    while n > 0:
        n //= 2
        total += n
    return total

n, m = map(int, input().split())
answer = min(count_five(n) - count_five(n - m) - count_five(m), count_two(n) - count_two(n - m) - count_two(m))
print(answer)