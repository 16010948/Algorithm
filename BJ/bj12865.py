n, k = map(int, input().split())

weights, values = [], []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(k + 1):
        if weights[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[-1][-1])