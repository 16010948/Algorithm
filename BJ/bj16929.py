deltas = ((0, -1), (-1, 0), (0, 1), (1, 0))

def is_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < m

def dfs(dot, start_y, start_x, y, x, count):
    for delta in deltas:
        ny = y + delta[0]
        nx = x + delta[1]
        if is_range(ny, nx) and dots[ny][nx] == dot:
            if not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(dot, start_y, start_x, ny, nx, count + 1)
                visited[ny][nx] = False
            elif ny == start_y and nx == start_x and count + 1 >= 4:
                print("Yes")
                exit()

n, m = map(int, input().split())

dots = []
for _ in range(n):
    dots.append(list(input()))

visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(dots[i][j], i, j, i, j, 1)
        visited[i][j] = False

print("No")