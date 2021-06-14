T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    if n % 2 == 1:
        print("#" + str(test_case), "Odd")
    else:
        print("#" + str(test_case), "Even")