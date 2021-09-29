from _collections import deque
INF = int(1e9)
SAFE = 0
WALL = 1
VIRUS = 2
NEW_VIRUS = 3

deltas = ((-1, 0), (0, -1), (1, 0), (0, 1))

def is_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < n

def init(queue, selected, visited):
    for i in range(virus_count):
        if selected[i]:
            queue.append((virus[i][0], virus[i][1], 0))
            visited[virus[i][0]][virus[i][1]] = True

def spread_virus(selected):
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    init(queue, selected, visited)

    time = 0
    spread = 0
    while queue:
        current = queue.popleft()
        for delta in deltas:
            ny = current[0] + delta[0]
            nx = current[1] + delta[1]
            time = current[2]
            if is_range(ny, nx) and (lab[ny][nx] == SAFE or lab[ny][nx] == VIRUS) and not visited[ny][nx]:
                visited[ny][nx] = True
                spread += 1
                queue.append((ny, nx, current[2] + 1))
    return (time, spread)


def select_virus(idx, cnt):
    global answer, virus
    if cnt > m:
        return

    if idx == virus_count:
        if cnt == m:
            time, spread = spread_virus(selected)
            if safe - m == spread:
                answer = min(answer, time)
        return
    selected[idx] = True
    lab[virus[idx][0]][virus[idx][1]] = NEW_VIRUS
    select_virus(idx + 1, cnt + 1)
    selected[idx] = False
    lab[virus[idx][0]][virus[idx][1]] = VIRUS
    select_virus(idx + 1, cnt)

n, m = map(int, input().split())

lab = []
safe = 0
virus = []
for i in range(n):
    lab.append(list(map(int, input().split())))
    for j in range(n):
        if lab[i][j] == SAFE or  lab[i][j] == VIRUS:
            safe += 1
        if lab[i][j] == VIRUS:
            virus.append((i, j))

virus_count = len(virus)
answer = INF
selected = [False] * virus_count
select_virus(0, 0)

if answer == INF:
    print(-1)
else:
    print(answer)