def find(u, parent):
    if u != parent[u]:
        parent[u] = find(parent[u], parent)
    return parent[u]


def union(u, v, parent):
    root1 = find(u, parent)
    root2 = find(v, parent)
    parent[root2] = root1


def solution(n, costs):
    LENGTH = len(costs)
    answer = 0

    costs.sort(key=lambda x: x[2])

    parent = [0]
    for i in range(1, n + 1):
        parent.append(i)

    edges = 0
    for i in range(LENGTH):
        u, v, weight = costs[i]
        if find(u, parent) != find(v, parent):
            union(u, v, parent)
            answer += weight

    return answer