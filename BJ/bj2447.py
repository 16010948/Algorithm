def print_rec(n):
    RANGE = (0, n + 1)
    for i in range(n + 2):
        for j in range(n + 2):
            if i in RANGE or j in RANGE:
                print("*", end='')
            else:
                print(" ", end='')
        print()

def make_rec(n):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1 and n // 3 != 0:
                make_rec(n // 3)
            print_rec(n)

n = int(input())
make_rec(n // 3)
