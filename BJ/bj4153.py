while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    if a < b:
        if b < c:
            heru = c
            ausar = a
            auset = b
        else:
            heru = b
            ausar = a
            auset = c
    else:
        if c < a:
            heru = a
            ausar = b
            auset = c
        else:
            heru = c
            ausar = a
            auset = b

    if ausar ** 2 + auset ** 2 == heru ** 2:
        print("right")
    else:
        print("wrong")