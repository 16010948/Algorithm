from collections import deque

def get_no_indegree(indegree):
    queue = deque()
    for v in range(1, n + 1):
        if indegree[v] == 0:
            indegree[v] = -1
            queue.append(v)
    return queue

def topological_sort(graph, indegree):
    queue = get_no_indegree(indegree)
    order = []

    for _ in range(n):
        if len(queue) > 1:
            print("?")
            return None

        if not queue:
            print("IMPOSSIBLE")
            return None


        cur = queue.popleft()
        order.append(cur)
        for v in range(1, n + 1):
            if graph[v][cur]:
                graph[v][cur] = False
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
    print(" ".join(str(o) for o in order))


tc = int(input())

for _ in range(tc):
    n = int(input())

    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0 for i in range(n + 1)]

    rank = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[rank[j]][rank[i]] = True
            indegree[rank[j]] += 1

    m = int(input())
    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1][v2], graph[v2][v1] = graph[v2][v1],  graph[v1][v2]
        if graph[v1][v2]:
            indegree[v1] += 1
            indegree[v2] -= 1
        else:
            indegree[v2] += 1
            indegree[v1] -= 1

    topological_sort(graph, indegree)

