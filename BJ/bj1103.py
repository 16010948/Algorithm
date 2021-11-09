import sys
sys.setrecursionlimit(10 ** 6)

deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

def is_range(position):
    return position[0] >= 0 and position[0] < n and position[1] >= 0 and position[1] < m

def dfs(cur):
    if visited[cur[0]][cur[1]]:
        return -1

    if dp[cur[0]][cur[1]] != -1:
        return dp[cur[0]][cur[1]]

    visited[cur[0]][cur[1]] = True
    dp[cur[0]][cur[1]] = 1
    for delta in deltas:
        ny = cur[0] + (delta[0] * int(coin[cur[0]][cur[1]]))
        nx = cur[1] + (delta[1] * int(coin[cur[0]][cur[1]]))
        if is_range((ny, nx)) and coin[ny][nx] != 'H':
            cnt = dfs((ny, nx))
            if cnt == -1:
                return -1

            dp[cur[0]][cur[1]] = max(dp[cur[0]][cur[1]], cnt + 1)

    visited[cur[0]][cur[1]] = False

    return dp[cur[0]][cur[1]]

n, m = map(int, input().split())

coin = []
for i in range(n):
    coin.append(list(input()))

visited = [[False] * m for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
print(dfs((0, 0)))