INF = int(1e9)
def combination(idx, count):
    global answer
    if count == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(i + 1, n):
                if visited[i] and visited[j]:
                    start += team[i][j] + team[j][i]
                if not visited[i] and not visited[j]:
                    link += team[i][j] + team[j][i]
        answer = min(answer, abs(start - link))
        return

    for i in range(idx, n):
        visited[i] = True
        combination(i + 1, count + 1)
        visited[i] = False

n = int(input())

team = []
for _ in range(n):
    team.append(list(map(int, input().split())))

answer = INF
visited = [False] * n
combination(0, 0)
print(answer)