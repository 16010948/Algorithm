# 처음 위치는 (1, 1)이며 미로의 출구는 (N, M)
# 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시
# 탈출하기 위해 움직여야 하는 최소 칸의 개수(시작 칸과 마지막 칸을 모두 포함하여 계산)

def bfs(x, y):
    queue = [(x, y)]
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while queue:
        x, y = queue.pop(0)
        for direction in directions:
            nx = x + direction[0]
            ny = y + direction[1]

            if nx < 0 or ny < 0 or nx >= row or ny >= col or maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

row, col = map(int, input().split())

maze = []
for i in range(row):
    maze.append(list(map(int, input())))
bfs(0, 0)

print(maze[row-1][col-1])