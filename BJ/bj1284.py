while True:
    house = int(input())
    if house == 0:
        break
    size = 1
    while house > 0:
        n = house % 10

        if n == 1:
            size += 2 + 1
        elif n == 0:
            size += 4 + 1
        else:
            size += 3 + 1
        house //= 10
    print(size)