def assign_hotel(h, w, n):
    y = n % h
    if y != 0:
        x = (n // h) + 1
    else:
        y = h
        x = n // h
    return y * 100 + x

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    print(assign_hotel(h, w, n))
