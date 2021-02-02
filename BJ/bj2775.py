t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    apart = [[0]*n for _ in range(k + 1)]
    apart[0] = list(range(1, n + 1))

    for i in range(1, k + 1):
        for j in range(n):
            if j > 0:
                apart[i][j] = apart[i][j-1] + apart[i - 1][j]
            else:
                apart[i][j] = apart[i - 1][j]
    print(apart[k][n - 1])