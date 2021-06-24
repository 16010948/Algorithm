def divide_11(n):
    count = 0
    while n % 11 == 0:
        n //= 11
        count += 1
    return [count, n]

def divide_7(n):
    count = 0
    while n % 7 == 0:
        n //= 7
        count += 1
    return [count, n]

def divide_5(n):
    count = 0
    while n % 5 == 0:
        n //= 5
        count += 1
    return [count, n]

def divide_3(n):
    count = 0
    while n % 3 == 0:
        n //= 3
        count += 1
    return [count, n]

def divide_2(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return [count, n]

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    a, n = divide_2(n)
    b, n = divide_3(n)
    c, n = divide_5(n)
    d, n = divide_7(n)
    e, n = divide_11(n)
    print("#" + str(test_case), a, b, c, d, e)