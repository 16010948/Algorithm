T = int(input())

for test_case in range(1, T + 1):
    total = 0
    for num in map(int, input().split()):
        if num % 2 == 1:
            total += num
    print("#"+str(test_case), total)