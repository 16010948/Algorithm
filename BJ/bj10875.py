def turn_dir(dx, dy):
    if dx == 0:
        dx, dy = dy, dx
    else:
        dy = dx * -1
        dx = 0
    return dx, dy

l = int(input())
size = (2 * l) + 1

cor = [[False] * size for _ in range(size)]
cor[l][l] = True

x, y = l, l
dx, dy = 0, 1
count = 1
n = int(input())
for _ in range(n):
    t, dir = input().split()
    for __ in range(int(t)):
        x = x + dx
        y = y + dy
        if cor[x][y] or (x < 0 or y < 0 or x >= size or y >= size):
            cor[l][l] = False
            break
        cor[x][y] = True
        count += 1
    if not cor[l][l]:
        break
    if dir == 'L':
        dx, dy = dx * -1, dy * -1
    dx, dy = turn_dir(dx, dy)
print(count)