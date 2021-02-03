t = int(input())
coordinate = []
for _ in range(t):
    coordinate.append(tuple(map(int, input().split())))
sorted_coordinate = sorted(coordinate, key = lambda c : (c[0], c[1]))
for c in sorted_coordinate:
    print(c[0], c[1])