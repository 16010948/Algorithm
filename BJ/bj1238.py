import heapq

INF = int(1e9)

def dijkstra(relation, start):
    distances = [INF] * (n + 1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        cur_w, cur_v = heapq.heappop(queue)
        if distances[cur_v] < cur_w:
            continue

        for edge in relation[cur_v]:
            new_dist = cur_w + edge.w
            if new_dist < distances[edge.v]:
                distances[edge.v] = new_dist
                heapq.heappush(queue, [new_dist, edge.v])
    return distances

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w

n, m, x = map(int, input().split())

relation = [[] for _ in range(n + 1)]
for _ in range(m):
    start, end, weight = map(int, input().split())
    relation[start].append(Edge(end, weight))

time = [0] * (n + 1)
for student in range(1, n + 1):
    distances = dijkstra(relation, student)

    if student == x:
        for i in range(1, n + 1):
            time[i] += distances[i]
    else:
        time[student] += distances[x]

print(max(time))