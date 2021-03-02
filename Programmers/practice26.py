def solution(a, b):
    for i in range(b):
        for j in range(a):
            print("*", end="")
        print()

a, b = map(int, input().strip().split(' '))
solution(a, b)