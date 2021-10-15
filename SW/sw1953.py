from collections import deque

DELTAS = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
)

TUNNEL = (
    (1, 2, 5, 6),
    (1, 2, 4, 7),
    (1, 3, 4, 5),
    (1, 3, 6, 7)
)

DIRECTION = (
    (0),
    (1, 1, 1, 1),
    (1, 1, 0, 0),
    (0, 0, 1, 1),
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 1, 1, 0),
    (1, 0, 1, 0)
)

def is_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < M

def bfs(r, c, l):
    visited = [[False] * M for _ in range(N)]

    queue = deque([[r, c, 1]])
    visited[r][c] = True

    cnt = 0
    while queue:
        cur = queue.popleft()
        cnt += 1
        if cur[2] < l:
            for i in range(len(DELTAS)):
                nr = cur[0] + DELTAS[i][0]
                nc = cur[1] + DELTAS[i][1]
                if is_range(nr, nc) and not visited[nr][nc] and under[nr][nc] != 0:
                    if DIRECTION[under[cur[0]][cur[1]]][i] == 1:
                        for tunnel in TUNNEL[i]:
                            if under[nr][nc] == tunnel:
                                visited[nr][nc] = True
                                queue.append([nr, nc, cur[2] + 1])
                                break
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    under = []
    for _ in range(N):
        under.append(list(map(int, input().split())))
    answer = bfs(R, C, L)
    print("#" + str(test_case), answer)