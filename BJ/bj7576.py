import sys
from collections import deque
input = sys.stdin.readline

deltas = ((-1, 0), (0, -1), (1, 0), (0, 1))
def init(queue):
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 1:
                queue.append((i, j, 0))

def is_range(y, x):
    return y >= 0 and y < n and x >= 0 and x < m

def bfs():
    global answer, count
    queue = deque()
    init(queue)
    while queue:
        cur = queue.popleft()
        count += 1
        for delta in deltas:
            ny = cur[0] + delta[0]
            nx = cur[1] + delta[1]
            answer = cur[2]
            if is_range(ny, nx) and tomato[ny][nx] == 0:
                tomato[ny][nx] = 1
                queue.append((ny, nx, cur[2] + 1))


m, n = map(int, input().split())

tomato = []
total = 0
for i in range(n):
    tomato.append(list(map(int, input().split())))
    for j in range(m):
        if tomato[i][j] != -1:
            total += 1

count = 0
answer = 0
bfs()
print(answer if total == count else -1)