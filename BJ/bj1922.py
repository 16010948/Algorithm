INF = int(1e9)

def find(parent, v):
    if parent[v] == v:
        return v
    parent[v] = find(parent, parent[v])
    return parent[v]

def union(parent, v1, v2):
    root1 = find(parent, v1)
    root2 = find(parent, v2)
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2

N = int(input())
M = int(input())

edges = []
for _ in range(M):
    v1, v2, weight = map(int, input().split())
    edges.append((weight, v1, v2))

edges.sort()

parent = [i for i in range(N + 1)]
result = 0
for edge in edges:
    weight, v1, v2 = edge
    if find(parent, v1) != find(parent, v2):
        union(parent, v1, v2)
        result += weight

print(result)