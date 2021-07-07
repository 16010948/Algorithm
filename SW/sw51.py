T = int(input())

for test_case in range(1, T + 1):
    sides = list(map(int, input().split()))
    count = {}
    for side in sides:
        if side in count:
            count[side] += 1
        else:
            count[side] = 1
    for key in count:
        if count[key] % 2 == 1:
            print("#%d %d"%(test_case, key))
            break