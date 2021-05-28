n = int(input())
dp = [0] * (n + 1)

for i in range(4, n + 1):
    sqrt_i = int(i ** 0.5)
    if i % sqrt_i == 0:
        dp[i] = dp[i - 1] + sqrt_i - 1
    elif (i - 1) % sqrt_i == 0:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1] + (i - 1) % sqrt_i

print(dp[-1])