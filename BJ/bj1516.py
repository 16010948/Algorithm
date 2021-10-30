from collections import deque

n = int(input())

graph = [[0] for _ in range(n + 1)]
cost = [0]
queue = deque()
degree = [0] * (n + 1)
answer = [0] * (n + 1)
for i in range(1, n + 1):
    vertexes = list(map(int, input().split()))
    cost.append(vertexes[0])
    for j in range(1, len(vertexes) - 1):
        graph[vertexes[j]].append(i)
        degree[i] += 1

for i in range(1, n + 1):
    if degree[i] == 0:
        queue.append(i)
        answer[i] = cost[i]

while queue:
    cur = queue.popleft()
    for adj in graph[cur]:
        answer[adj] = max(answer[adj], cost[adj] + answer[cur])
        degree[adj] -= 1

        if degree[adj] == 0:
            queue.append(adj)

for i in range(1, n + 1):
    print(answer[i])