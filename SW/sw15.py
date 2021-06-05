SIZE = 5

for i in range(SIZE):
    for j in range(SIZE):
        if i == j:
            print("#", end="")
        else:
            print("+", end="")
    print()