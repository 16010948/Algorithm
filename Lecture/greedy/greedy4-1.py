n = int(input())
directions = input().split()

x, y = 1, 1
dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)
MOVE_TYPES = ('L', 'R', 'U', 'D')

for direction in directions:
    for i in range(len(MOVE_TYPES)):
        if direction == MOVE_TYPES[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            break

    if nx > 0 and nx <= n and ny > 0 and ny <= n:
        x = nx
        y = ny

print(x, y)