# 채굴자가 오른쪽 위, 오른쪽, 오른쪽 아래 방향으로 이동하여 얻을 수 있는 금의 최대 크기
def check_max(m, array):
    result = 0
    for row in array:
        result = max(row[m - 1], result)
    return result

def mine(dp, n, m):
    for i in range(1, m):
        for j in range(n):
            # 왼쪽 위에서 오는 경우
            if j > 0: left_up = dp[j - 1][i - 1]
            else: left_up = 0
            # 왼쪽 아래에서 오는 경우
            if j < n - 1: left_down = dp[j + 1][i - 1]
            else: left_down = 0
            # 왼쪽에서 오는 경우
            left = dp[j][i - 1]
            dp[j][i] += max(left_up, left, left_down)
    return check_max(m, dp)

for tc in range(int(input())):
    n, m = map(int, input().split())
    gold = list(map(int, input().split()))
    dp = []
    for i in range(n):
        dp.append(gold[(i*m):((i+1)*m)])
    print(mine(dp, n, m))