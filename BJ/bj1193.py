def get_fraction(n):
    i = 1
    up = False
    total = 0

    while total < n:
        total += i
        up = not up
        i += 1
    i -= 1

    if up:
        numerator = 1 + total - n
        denominator = i - total + n
    else:
        numerator = i - total + n
        denominator = 1 + total - n

    return (numerator, denominator)

n = int(input())
fraction = get_fraction(n)
print(str(fraction[0])+'/'+str(fraction[1]))

