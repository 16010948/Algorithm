LENGTH = 10
T = int(input())

for test_case in range(1, T + 1):
    array = list(map(int, input().split()))
    print("#%d %d"%(test_case, round(sum(array) / LENGTH, 0)))
