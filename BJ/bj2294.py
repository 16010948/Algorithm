MAX = 10001
n, k = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(int(input()))
coin = sorted(list(set(coin)))

dp = [MAX] * (k + 1)
for i in range(1, k + 1):
    for c in coin:
        if i - c >= 0:
            dp[i] = dp[i - c] + 1
        if i % c == 0:
            dp[i] = min(i // c, dp[i])
print(-1 if dp[k] == MAX else dp[k])