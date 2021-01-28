# 1번 회사에서 출발하여 k번 회사를 방문한 뒤에 x번 회사로 가는 방법
INF = int(1e9)
n, m = map(int, input().split())
distance = [[INF] * n for _ in range(n)]

for i in range(n):
    distance[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    distance[a - 1][b - 1] = 1
    distance[b - 1][a - 1] = 1

x, k = map(int, input().split())

for c in range(n):
    for a in range(n):
        for b in range(n):
            distance[a][b] = min(distance[a][b], distance[a][c] + distance[c][b])

result = distance[0][k - 1] + distance[k - 1][x - 1]
if result >= INF:
    print(-1)
else:
    print(result)


