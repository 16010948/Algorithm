T = int(input())
for test_case in range(1, T + 1):
    array = list(map(int, input().split()))
    max_value = 0
    for value in array:
        if value > max_value:
            max_value = value
    print("#"+str(test_case), max_value)