from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([1])

    visited = [False] * (n + 1)
    while queue:
        cur = queue.popleft()
        for adj in edge[cur]:
            if adj != 1 and not visited[adj]:
                visited[adj] = True
                queue.append(adj)
                parent[adj] = cur

n = int(input())

edge = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

parent = [0] * (n + 1)
bfs()

for i in range(2, n + 1):
    print(parent[i])