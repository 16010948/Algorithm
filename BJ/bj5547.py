from collections import deque

even_deltas = ((0, -1), (-1, 0), (-1, -1), (0, 1), (1, 0), (1, -1))
odd_deltas = ((0, -1), (-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1))

def is_range(y, x):
    return y >= 0 and y <= h + 1 and x >= 0 and x <= w + 1

def bfs():
    queue = deque([(0, 0)])

    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = True
    count = 0
    while queue:
        y, x = queue.popleft()

        if y % 2 == 0:
            deltas = even_deltas
        else:
            deltas = odd_deltas

        for delta in deltas:
            ny = y + delta[0]
            nx = x + delta[1]
            if is_range(ny, nx):
                if not visited[ny][nx] and wall[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                elif wall[ny][nx] == 1:
                    count += 1
    return count

w, h = map(int, input().split())
wall = [[0] * (w + 2)]
for _ in range(h):
    wall.append([0] + list(map(int, input().split())) + [0])
wall.append([0] * (w + 2))

answer = bfs()
print(answer)