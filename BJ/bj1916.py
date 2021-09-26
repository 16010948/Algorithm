import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []

    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, cur = heapq.heappop(queue)

        if distance[cur] < dist:
            continue

        for vertex, weight in graph[cur]:
            cost = dist + weight

            if cost < distance[vertex]:
                heapq.heappush(queue, (cost, vertex))
                distance[vertex] = cost

n = int(input())
m = int(input())

graph=[[] for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

start, end = map(int, input().split())
distance = [INF] * (n + 1)
dijkstra(start)
print(distance[end])