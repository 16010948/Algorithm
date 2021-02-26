n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))

count = 0

for i in range(n - 1, -1, -1):
    count += k // coin[i]
    k = k % coin[i]
print(count)