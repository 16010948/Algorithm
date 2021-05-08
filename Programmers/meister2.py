dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)


def bfs(maps):
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for _ in range(m)]
    queue = [(0, 0, 1)]
    visited[0][0] = True
    result = 10001

    while queue:
        x, y, count = queue.pop(0)

        if x == n - 1 and y == m - 1:
            result = min(result, count)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and not visited[ny][nx] and maps[ny][nx] == 1:
                queue.append((nx, ny, count + 1))
                visited[ny][nx] = True
    return result


def solution(maps):
    answer = 0
    answer = bfs(maps)

    if answer > 10000:
        answer = -1

    return answer

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# answer = 11
print(solution(maps))

maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
# answer = -1
print(solution(maps))