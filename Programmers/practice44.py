def solution(s):
    N = len(s)
    answer = 1

    dp = [[False] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = True
        if i > 0 and s[i - 1] == s[i]:
            dp[i - 1][i] = True
            answer = 2

    for i in range(2, N):
        for j in range(N - i):
            if s[j] == s[j + i] and dp[j + 1][j + i - 1]:
                dp[j][j + i] = True
                answer = max(answer, i + 1)

    return answer