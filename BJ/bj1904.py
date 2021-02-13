n = int(input())
tile1 = 1
tile2 = 1
result = 1
for n in range(2, n + 1):
    result = (tile1 + tile2) % 15746
    tile1 = tile2
    tile2 = result
print(result)