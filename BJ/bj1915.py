n, m = map(int, input().split())

arr = []
dp = [[0] * m for _ in range(n)]
answer = 0
for i in range(n):
    arr.append(list(map(int, input())))
    for j in range(m):
        if arr[i][j] == 1:
            dp[i][j] = arr[i][j]
            answer = 1

for y in range(1, n):
    for x in range(1, m):
        if arr[y][x] == 1:
            if dp[y - 1][x] != 0 and dp[y][x - 1] != 0 and dp[y - 1][x - 1] != 0:
                dp[y][x] = min(dp[y - 1][x], dp[y][x - 1], dp[y - 1][x - 1]) + 1
                answer = max(answer, dp[y][x])

print(answer * answer)