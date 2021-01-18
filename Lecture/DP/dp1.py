# 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소 한 칸 이상 떨어진 식량 창고를 약탈
# 개미가 얻을 수 있는 식량의 최댓값을 구하는 프로그램
n = int(input())
warehouse = list(map(int, input().split()))
dp = [0] * n

# 다이나믹 프로그래밍 진행 (보텀업)dp[0] = warehouse[0]
dp[1] = max(warehouse[0],warehouse[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+warehouse[i])

print(dp[n - 1])