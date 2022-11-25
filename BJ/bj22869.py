n, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [False] * n
dp[0] = True

for i in range(n - 1):
    for j in range(i + 1, n):
        if dp[i] and (j - i) * (1 + abs(a[j] - a[i])) <= k:
            dp[j] = True

print("YES" if dp[n - 1] else "NO")