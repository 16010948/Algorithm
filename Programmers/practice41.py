COL_SIZE = 4


def solution(land):
    answer = 0
    dp = [[0] * COL_SIZE for _ in range(len(land))]

    dp[0] = land[0]

    for i in range(1, len(land)):
        dp[i][0] = land[i][0] + max(dp[i - 1][1], dp[i - 1][2], dp[i - 1][3])
        dp[i][1] = land[i][1] + max(dp[i - 1][0], dp[i - 1][2], dp[i - 1][3])
        dp[i][2] = land[i][2] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][3])
        dp[i][3] = land[i][3] + max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])

    answer = max(dp[-1])
    return answer

land = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
# answer = 16
print(solution(land))