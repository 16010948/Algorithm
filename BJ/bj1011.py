import math
t = int(input())

result = []

for _ in range(t):
    x, y = map(int, input().split())
    gap = y - x
    sqrt = int(math.sqrt(gap))
    if sqrt ** 2 == gap:
        result.append(sqrt + sqrt - 1)
    elif (sqrt ** 2) + sqrt >= gap:
        result.append(sqrt + sqrt)
    else:
        result.append(sqrt + sqrt + 1)

for r in result:
    print(r)