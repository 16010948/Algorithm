from _collections import deque

deltas = ((-1, 1), (1, 1), (0, 2))
INF = int(1e9)

def is_range(n):
    return n >= 0 and n <= RANGE

def bfs(start):
    global answer
    queue = deque([start])
    dp[start] = 0
    while queue:
        cur = queue.popleft()
        if cur == K:
            answer += 1

        for delta in deltas:
            moved = (cur + delta[0]) * delta[1]
            if is_range(moved):
                if dp[moved] >= dp[cur] + 1:
                    dp[moved] = dp[cur] + 1
                    if moved == cur:
                        answer += 1
                    else:
                        queue.append(moved)

N, K = map(int, input().split())
RANGE = max(N, K) + 1

answer = 0
dp = [INF] * (RANGE + 1)
bfs(N)
print(dp[K])
print(answer)