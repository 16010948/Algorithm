T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    dp = [1] * (m + 1)
    for i in range(2, m + 1):
        dp[i] = dp[i - 1] * i
    print(dp[m] // (dp[n] * dp[m - n]))