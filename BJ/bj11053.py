n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
count = [0] * n
dp[0] = arr[0]
count[0] = 1
max_count = 0
for i in range(1, n):
    if arr[i - 1] < arr[i]:
        dp[i] = arr[i]
        count[i] = count[i - 1] + 1
    else:
        dp[i] = arr[i - 1]
        count[i] = count[i - 1]

print(dp)
print(count)