deltas = ((-1, 0), (0, -1), (0, 1), (1, 0))
def bfs(r, c, color_list):
    queue = [[r, c]]
    visited[r][c] = True
    while queue:
        cur = queue.pop(0)
        for delta in deltas:
            nr = cur[0] + delta[0]
            nc = cur[1] + delta[1]
            if nr >= 0 and nr < n and nc >= 0 and nc < n and not visited[nr][nc] and color[nr][nc] in color_list:
                visited[nr][nc] = True
                queue.append([nr, nc])



n = int(input())

color = []
for _ in range(n):
    color.append(input())

normal = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            normal += 1
            bfs(i, j, (color[i][j]))

blind = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            blind += 1
            if color[i][j] in ('R', 'G'):
                color_list = ('R', 'G')
            else:
                color_list = (color[i][j])
            bfs(i, j, color_list)
print(normal, blind)