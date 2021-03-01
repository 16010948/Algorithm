n, k = map(int, input().split())
Josephus = list(range(1, n + 1))

index = 0
result = []
while len(result) < n:
    index = (index + k - 1) % len(Josephus)
    result.append(Josephus.pop(index))

print("<" + str(result)[1:-1] + ">")