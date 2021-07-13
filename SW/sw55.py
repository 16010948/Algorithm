T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    s = (n * (n + 1)) // 2
    print("#%d %d %d %d"%(test_case, s, 2 * s - n, 2 * s))
