def bfs(start):
    queue = []
    queue.append(start)
    visited[start] = True

    cnt = 0
    while queue:
        cur = queue.pop(0)
        for adj in graph[cur]:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = True
                cnt += 1
    return cnt

n = int(input())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

cnt = bfs(1)
print(cnt)