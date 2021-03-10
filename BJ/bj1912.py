n = int(input())
array = list(map(int, input().split()))
dp = [0] * n
dp[0] = array[0]
max_total = array[0]
for i in range(1, n):
    dp[i] = max(dp[i - 1] + array[i], array[i])
    max_total = max(max_total, dp[i])
print(max_total)