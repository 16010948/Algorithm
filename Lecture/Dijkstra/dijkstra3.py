# 도시 c에서 보낸 메시지를 받게 되는 도시의 개수와 도시들이 모두 메시지를 받는 데까지 걸리는 시간을 반환
import heapq

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] > dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e9)
n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dijkstra(c)

count = 0
max_distance = 0
for i in range(1, n + 1):
    if  distance[i] != INF:
        count += 1
        max_distance = max(max_distance, distance[i])

print(count - 1, max_distance)
