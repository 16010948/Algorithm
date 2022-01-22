n = int(input())
find = int(input())

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
snail = [[0] * n for _ in range(n)]
value = 1
length = 1
direction = 0
y = n // 2
x = n // 2
find_y = -1
find_x = -1
while value <= n * n:
    for i in range(length):
        snail[y][x] = value
        if value == find:
            find_y = y
            find_x = x
        value += 1
        y += delta[direction][0]
        x += delta[direction][1]
    direction = (direction + 1) % 4
    if direction % 2 == 0:
        length += 1

for i in range(n):
    for j in range(n):
        print(snail[i][j], end=' ')
    print()
print(find_y + 1, find_x + 1)