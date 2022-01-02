n = int(input())

doubles = []
for _ in range(n):
    doubles.append(float(input()))

dp = [0] * n
dp[0] = doubles[0]
answer = 0
for i in range(1, n):
    dp[i] = max(doubles[i], dp[i - 1] * doubles[i])
    answer = max(answer, dp[i])
print("%.3f" % answer)