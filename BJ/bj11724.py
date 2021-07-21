import sys
input = sys.stdin.readline

def bfs(start):
    queue = [start]
    while queue:
        cur = queue.pop()
        visited[cur] = True
        for node in graph[cur]:
            if not visited[node]:
                queue.append(node)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        answer += 1
print(answer)