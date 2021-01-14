def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v-1] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v-1]:
        if not visited[i-1]:
            dfs(graph, i, visited)

graph = [
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
visited = [False] * 8

dfs(graph, 1, visited)