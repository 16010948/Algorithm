import sys
input = sys.stdin.readline

class Consulting:
    def __init__(self, t, p):
        self.t = t
        self.p = p

n = int(input())

work = []
for _ in range(n):
    t, p = map(int, input().split())
    work.append(Consulting(t, p))

dp = [0] * (n + 1)
for i in range(n):
    if work[i].t + i <= n:
        dp[i + work[i].t] = max(dp[i + work[i].t], dp[i] + work[i].p)

    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])