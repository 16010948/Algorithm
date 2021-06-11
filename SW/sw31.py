T = int(input())

for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    array = ["0"] * n
    for i in range(1, q + 1):
        l, r = map(int, input().split())
        for j in range(l - 1, r):
            array[j] = str(i)
    print("#" + str(test_case), " ".join(array))