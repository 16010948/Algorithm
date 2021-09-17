n = int(input())
arr = list(map(int, input().split()))

answer = 0
dp = [0] * n
for i in range(n):
    dp[i] = arr[i]
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
    answer = max(answer, dp[i])
print(answer)