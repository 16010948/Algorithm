T = int(input())

for test_case in range(1, T + 1):
    hour1, minute1, hour2, minute2 = map(int, input().split())
    hour = (hour1 + hour2 + (minute1 + minute2) // 60) % 12
    minute = (minute1 + minute2) % 60

    if hour == 0:
        hour = 12
    print("#%d %d %d" % (test_case, hour, minute))