n = int(input())
coordinate = []
for _ in range(n):
    coordinate.append(tuple(map(int, input().split())))
sorted_coordinate = sorted(coordinate, key=lambda c:(c[1], c[0]))
for c in sorted_coordinate:
    print(c[0], c[1])