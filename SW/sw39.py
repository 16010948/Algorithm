T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    result = "1/{} ".format(n) * n
    print("#{} {}".format(test_case, result))