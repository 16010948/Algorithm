x, y, w, h = map(int, input().split())

d1 = abs(y - h)
d2 = abs(x - w)
d3 = abs(x)
d4 = abs(y)

print(min(d1, d2, d3, d4))