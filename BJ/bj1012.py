deltas = [[-1, 0], [0, -1], [0, 1], [1, 0]]
def dfs(r, c):
    cabbage[r][c] = 0
    for delta in deltas:
        nr = r + delta[0]
        nc = c + delta[1]
        if nr >= 0 and nr < n and nc >= 0 and nc < m and cabbage[nr][nc] == 1:
            dfs(nr, nc)

T = int(input())
for test_case in range(T):
    m, n, k = map(int, input().split())

    cabbage = [[0] * m for _ in range(n)]
    for _ in range(k):
        c, r = map(int, input().split())
        cabbage[r][c] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                answer += 1
                dfs(i, j)
    print(answer)