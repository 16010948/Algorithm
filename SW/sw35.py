T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    done = list(map(int, input().split()))
    student = [False] * (n + 1)
    for d in done:
        student[d] = True

    print("#" + str(test_case), end=" ")
    for i in range(1, n + 1):
        if not student[i]:
            print(i, end=" ")
    print()