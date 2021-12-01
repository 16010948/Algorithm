Z = 26

n = input()
length = len(n) + 1

dp = [0] * length
if n[0] == '0':
    print(0)
else:
    n = '0' + n
    dp[0] = dp[1] = 1
    for i in range(2, length):
        num = int(n[i - 1] + n[i])
        if n[i] != '0':
            dp[i] = dp[i - 1]
        if 10 <= num and num <= Z:
            dp[i] = (dp[i] + dp[i - 2]) % 1000000
    print(dp[-1])