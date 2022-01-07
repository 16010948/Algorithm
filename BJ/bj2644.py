from collections import deque

def bfs(start):
    queue = deque([(start, 0)])

    visited = [False] * 101
    visited[start] = True

    while queue:
        cur, depth = queue.popleft()

        if cur == b:
            return depth

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                queue.append((adj, depth + 1))
    return -1

n = int(input())
a, b = map(int, input().split())

m = int(input())
graph = {}
for _ in range(m):
    x, y = map(int, input().split())
    if x not in graph:
        graph[x] = {}
    graph[x][y] = 1

    if y not in graph:
        graph[y] = {}
    graph[y][x] = 1

print(bfs(a))