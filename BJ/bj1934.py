def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = int(input())

for _ in range(t):
    n1, n2 = map(int, input().split())
    g = gcd(n1, n2)
    print(g * (n1 // g) * (n2 // g))