T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    total = 0
    for _ in range(n):
        p, x = map(float, input().split())
        total += p * x
    print("#" + str(test_case), total)
