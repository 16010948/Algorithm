# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치하여 남아 있는 병사의 수가 최대가 되도록 할 때 열외시켜야 하는 병사의 수
n = int(input())
soldier = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if soldier[j] > soldier[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))