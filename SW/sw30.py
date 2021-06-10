T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    earnings = list(map(int, input().split()))
    avg = sum(earnings) // n

    count = 0
    for e in earnings:
        if e <= avg:
            count += 1
    print("#" + str(test_case), count)