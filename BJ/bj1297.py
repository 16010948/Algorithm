d, h, w = map(int, input().split())

d2 = d * d
h2 = h * h
w2 = w * w
proportion = (d2 / (h2 + w2)) ** 0.5

print(int(proportion * h), int(proportion * w))