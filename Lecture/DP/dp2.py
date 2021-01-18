# 정수 X가 주어졌을 때
# 1. X가 5로 나누어 떨어지면 5로 나눔
# 2. X가 3로 나누어 떨어지면 3로 나눔
# 3. X가 2로 나누어 떨어지면 2로 나눔
# 4. X에서 1을 뺌
# 4가지 연산을 사용하여 1로 만드는 연산을 하는 횟수의 최솟 값

x = int(input())

dp = [0] * (x + 1)
for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
print(dp[x])

