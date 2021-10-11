from _collections import deque

INF = int(1e9)

def is_range(n):
    return n >= 0 and n <= RANGE

def move(moved, cur, queue, cnt):
    if is_range(moved):
        if dp[moved] > dp[cur]:
            dp[moved] = dp[cur] + cnt
            if moved != K:
                queue.append(moved)

def bfs(start):
    queue = deque([start])
    dp[start] = 0

    while queue:
        cur = queue.popleft()

        moved = cur * 2
        move(moved, cur, queue, 0)

        moved = cur - 1
        move(moved, cur, queue, 1)

        moved = cur + 1
        move(moved, cur, queue, 1)

N, K = map(int, input().split())
RANGE = max(N, K) + 1

dp = [INF] * (RANGE + 1)
bfs(N)
print(dp[K])