import sys
sys.setrecursionlimit(1500)

def dfs(y, x):
    if y == n - 1 and x == m - 1:
        return 1

    if dp[y][x] == -1:
        dp[y][x] = 0
        for dy, dx in deltas:
            ny = y + dy
            nx = x + dx
            if ny >= 0 and ny < n and nx >= 0 and nx < m and maps[ny][nx] < maps[y][x]:
                dp[y][x] += dfs(ny, nx)
    return dp[y][x]

deltas = ((0, -1), (-1, 0), (0, 1), (1, 0))
n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dp = [[-1] * m for _ in range(n)]
print(dfs(0, 0))