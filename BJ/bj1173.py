N, m, M, T, R = map(int, input().split())

init = m
if m + T > M:
    print(-1)
else:
    time = 0
    while N > 0:
        if m + T <= M:
            m += T
            N -= 1
        else:
            m = max(init, m - R)
        time += 1
    print(time)