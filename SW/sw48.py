T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    flies = []
    for _ in range(n):
        flies.append(list(map(int, input().split())))

    answer = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            total = 0
            for k in range(m):
                for l in range(m):
                    total += flies[i + k][j + l]
            answer = max(answer, total)
    print("#%d %d" % (test_case, answer))