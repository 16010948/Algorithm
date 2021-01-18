# def combination_money(total):
#     if total > m:
#         return
#     for i in money:
#         if i + total > m:
#             continue
#         dp[i + total] = min(dp[total] + 1, dp[i + total])
#         combination_money(i + total)

# M원을 만들기 위한 최소한의 화폐 개수
n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))

dp = [10001] * (m + 1)
dp[0] = 0
# combination_money(0)

for i in range(n):
    for j in range(money[i], m + 1):
        if dp[j - money[i]] != 10001:
            dp[j] = min(dp[j], dp[j - money[i]] + 1)

if dp[m] < 10001:
    print(dp[m])
else:
    print(-1)