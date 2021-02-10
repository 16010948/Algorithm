n = int(input())
answer = 0
for i in range(1, n + 1):
    m = i
    total = m
    while m > 0:
        total += m % 10
        m //= 10

    if total == n:
        answer = i
        break

print(answer)