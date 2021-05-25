def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n = int(input())
rings = list(map(int, input().split()))
for i in range(1, n):
    d = gcd(rings[0], rings[i])
    print(str(rings[0] // d) + "/" + str(rings[i] // d))