from collections import deque
deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))

def is_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < m

def bfs(y, x, visited):
    queue = deque()
    queue.append((y, x))
    cnt = 0
    while queue:
        cur = queue.popleft()
        cnt += 1
        for delta in deltas:
            ny = cur[0] + delta[0]
            nx = cur[1] + delta[1]
            if is_range(ny, nx) and board[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
    return cnt

n, m, k = map(int, input().split())

board = [[0] * m for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            board[y][x] = 1

visited = [[False] * m for _ in range(n)]
area = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            area.append(bfs(i, j, visited))

print(len(area))
print(' '.join(list(map(str, sorted(area)))))