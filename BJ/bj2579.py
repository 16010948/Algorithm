n = int(input())
stair = [0] * (n + 1)
for i in range(1, n + 1):
    stair[i] = int(input())
dp = [0] * (n + 1)
for i in range(1, n + 1):
    if i == 1:
       dp[i] = stair[i]
    elif i == 2:
        dp[i] = stair[i - 1] + stair[i]
    else:
        dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i])
print(dp[n])