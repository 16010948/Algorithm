dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def move(board, x, y, dx, dy):
    count = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return [x, y], count

def bfs(board, visited, queue):
    while queue:
        red, blue, depth = queue.pop(0)
        if depth > 10:
            break
        for i in range(4):
            new_red, r_count = move(board, red[0], red[1], dx[i], dy[i])
            new_blue, b_count = move(board, blue[0], blue[1], dx[i], dy[i])
            if board[new_blue[0]][new_blue[1]] != 'O':
                if board[new_red[0]][new_red[1]] == 'O':
                    return 1
                if new_red[0] == new_blue[0] and new_red[1] == new_blue[1]:
                    if r_count > b_count:
                        new_red[0] -= dx[i]
                        new_red[1] -= dy[i]
                    else:
                        new_blue[0] -= dx[i]
                        new_blue[1] -= dy[i]
                if not visited[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]]:
                    visited[new_red[0]][new_red[1]][new_blue[0]][new_blue[1]] = True
                    queue.append((new_red, new_blue, depth + 1))
    return 0

n, m = map(int, input().split())

board = []
red = [-1, -1]
blue = [-1, -1]
for i in range(n):
    board.append(list(input()))
    if (-1 in red) or (-1 in blue):
        for j in range(m):
            if board[-1][j] == 'R':
                board[-1][j] = '.'
                red = [i, j]
            if board[-1][j] == 'B':
                board[-1][j] = '.'
                blue = [i, j]

visited = [[[[False] * m for _ in range(n)] for __ in range(m)] for ___ in range(n)]

queue = [(red, blue, 1)]
visited[red[0]][red[1]][blue[0]][blue[1]] = True
print(bfs(board, visited, queue))