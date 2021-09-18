INF = int(1e9)

n = int(input())
m = int(input())

D = [[INF] * n for _ in range(n)]
for _ in range(m):
    v1, v2, weight = map(int, input().split())
    D[v1 - 1][v2 - 1] = min(D[v1 - 1][v2 - 1], weight)

for v in range(n):
    for start in range(n):
        for end in range(n):
            D[start][end] = min(D[start][end], D[start][v] + D[v][end])

for i in range(n):
    for j in range(n):
        result = D[i][j]
        if i == j or result == INF:
            result = 0
        print(result, end=" ")
    print()