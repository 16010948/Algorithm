def merge_sort(array):
    n = len(array)
    if n <= 1:
        return
    mid = n // 2
    g1 = array[:mid]
    g2 = array[mid:]
    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2):
        if g1[i1] < g2[i2]:
            array[ia] = g1[i1]
            i1 += 1
        else:
            array[ia] = g2[i2]
            i2 += 1
        ia += 1

    for i in range(i1, len(g1)):
        array[ia] = g1[i]
        ia += 1

    for i in range(i2, len(g2)):
        array[ia] = g2[i]
        ia += 1

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        merge_sort(graph[v])
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    merge_sort(graph[v])
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

n, m, v = map(int, input().split())

graph = {}
for _ in range(m):
    v1, v2 = map(int, input().split())
    if v1 in graph.keys():
        graph[v1].append(v2)
    else:
        graph[v1] = [v2]

    if v2 in graph.keys():
        graph[v2].append(v1)
    else:
        graph[v2] = [v1]

visited = [False] * (n + 1)
dfs(graph, v, visited)
print()
visited = [False] * (n + 1)
bfs(graph, v, visited)
