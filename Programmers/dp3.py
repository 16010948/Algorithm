def solution(m, n, puddles):
    answer = 0
    route = [[0] * m for _ in range(n)]

    for puddle in puddles:
        if len(puddle) >= 2:
            route[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(n):
        for j in range(m):
            if route[i][j] < 0:
                route[i][j] = 0
            elif i > 0 or j > 0:
                if i > 0:
                    route[i][j] += route[i - 1][j]
                if j > 0:
                    route[i][j] += route[i][j - 1]
            else:
                route[i][j] = 1
            route[i][j] %= 1000000007
    answer = route[n - 1][m - 1]
    return answer

m = 4
n = 3
puddles = [[2, 2]]
# answer = 4
print(solution(m, n, puddles))