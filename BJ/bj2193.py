def fibonacci(n):
    if n > 2 and dp[n] == 1:
        dp[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return dp[n]

n = int(input())
dp = [1] * (n + 1)
print(fibonacci(n))