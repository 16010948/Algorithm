T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n < m:
        n, m = m, n
        a, b = b, a
    max_sum = 0
    for i in range(n - m + 1):
        s = 0
        for j in range(m):
            s += a[i + j] * b[j]
        max_sum = max(max_sum, s)
    print("#%d %d"%(test_case, max_sum))