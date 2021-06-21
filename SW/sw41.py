T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    hay = []
    s = 0
    for _ in range(n):
        hay.append(int(input()))
        s += hay[-1]
    avg = s // n

    answer = 0
    for h in hay:
        if h < avg:
            answer += avg - h
    print("#{} {}".format(test_case, answer))