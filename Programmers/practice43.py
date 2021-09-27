def solution(n, money):
    answer = 0
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(len(money)):
        for j in range(money[i], n + 1):
            dp[j] = (dp[j] + dp[j - money[i]]) % 1000000007
    answer = dp[n]
    return answer