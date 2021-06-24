T = int(input())

for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    cost = list(map(int, input().split()))

    min_cost = int(1e9)
    for i in range(n - l + 1):
        s = 0
        for j in range(i, n):
            s += cost[j]
            if j - i + 1 >= l:
                min_cost = min(min_cost, s / (j - i + 1))
    print("%.11f" % (min_cost))