dp = [0] * 101

def p(k):
    if dp[k] != 0:
        return dp[k]

    dp[k] = p(k - 2) + p(k - 3)
    return dp[k]

dp[1] = 1
dp[2] = 1
dp[3] = 1

n = int(input())

for _ in range(n):
    k = int(input())
    print(p(k))