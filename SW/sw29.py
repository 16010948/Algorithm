T = int(input())

for test_case in range(1, T + 1):
    total, a, b = map(int, input().split())
    max_inter = min(a, b)
    min_inter = max(a + b - total, 0)
    print("#"+str(test_case), max_inter, min_inter)