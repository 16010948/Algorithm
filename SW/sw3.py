T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = "No"
    for i in range(1, 9 + 1):
        if n % i == 0 and n // i < 10:
            result = "Yes"
            break
    print("#"+str(test_case), result)