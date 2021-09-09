from collections import deque
deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))
def bfs():
    dist = [[-1] * n for _ in range(m)]
    queue = deque()

    queue.append((0, 0))
    dist[0][0] = 0

    while queue:
        y, x = queue.popleft()
        for delta in deltas:
            ny = y + delta[0]
            nx = x + delta[1]
            if 0 <= ny and ny < m and 0 <= nx and nx < n and dist[ny][nx] == -1:
                if algo_spot[ny][nx] == 1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((ny, nx))
                else:
                    dist[ny][nx] = dist[y][x]
                    queue.appendleft((ny, nx))
    return dist[m - 1][n - 1]

n, m = map(int, input().split())
algo_spot = [list(map(int, list(input()))) for _ in range(m)]

answer = bfs()
print(answer)