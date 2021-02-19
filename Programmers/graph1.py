import heapq


def dijkstra(start, distance, graph):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = distance[now] + i[0]
            if distance[i[1]] > cost:
                distance[i[1]] = cost
                heapq.heappush(q, (cost, i[1]))


INF = int(1e9)


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for e in edge:
        graph[e[0]].append((1, e[1]))
        graph[e[1]].append((1, e[0]))

    dijkstra(1, distance, graph)
    answer = distance[1:].count(max(distance[1:]))

    return answer

n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# answer = 3
print(solution(n, vertex))


