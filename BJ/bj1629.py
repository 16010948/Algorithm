def f_pow(a, b, c):
    if b == 1:
        return a % c

    x = f_pow(a, b // 2, c)
    if b % 2 == 0:
        return (x * x) % c
    else:
        return (((x * x) % c) * a) % c

a, b, c = map(int, input().split())

print(f_pow(a, b, c))