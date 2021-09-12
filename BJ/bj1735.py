def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
numerator1, denominator1 = map(int, input().split())
numerator2, denominator2 = map(int, input().split())

numerator = numerator1 * denominator2 + numerator2 * denominator1
denominator = denominator1 * denominator2

g = gcd(numerator, denominator)

print(numerator // g, denominator // g)