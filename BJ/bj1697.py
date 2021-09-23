INF = 100001
def bfs(n, k):
    queue = []
    dp[n] = 0
    queue.append(n)
    while queue:
        cur = queue.pop(0)
        if cur == k:
            break
        if cur - 1 >= 0 and dp[cur - 1] == INF:
            dp[cur - 1] = min(dp[cur - 1], dp[cur] + 1)
            queue.append(cur - 1)
        if cur + 1 < INF and dp[cur + 1] == INF:
            dp[cur + 1] = min(dp[cur + 1], dp[cur] + 1)
            queue.append(cur + 1)
        if cur * 2 < INF and dp[cur * 2] == INF:
            dp[cur * 2] = min(dp[cur * 2], dp[cur] + 1)
            queue.append(cur * 2)


n, k = map(int, input().split())

dp = [INF] * (INF + 1)
bfs(n, k)
print(dp[k])

