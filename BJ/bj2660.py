INF = int(1e9)
n = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
while True:
    candidate1, candidate2 = map(int, input().split())
    if candidate1 < 0 and candidate2 < 0:
        break

    graph[candidate1][candidate2] = graph[candidate2][candidate1] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        graph[i][i] = 0
        for j in range(1, n + 1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
min_score = n
answer = []
for i in range(1, n + 1):
    max_score = 0
    for j in range(1, n + 1):
        max_score = max(max_score, graph[i][j])
    if max_score < min_score:
        min_score = max_score
        answer = [i]
    elif max_score == min_score:
        answer.append(i)

print(min_score, len(answer))
print(' '.join(str(item) for item in answer))