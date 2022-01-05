def dfs(s, idx):
    if idx == n:
        if s > 0:
            is_able[s] = True
        return
    dfs(s, idx + 1)
    dfs(s + weight[idx], idx + 1)
    dfs(s - weight[idx], idx + 1)

n = int(input())
weight = list(map(int, input().split()))
total = sum(weight)

is_able = [False] * (total + 1)
dfs(0, 0)

count = 0
for i in range(1, total + 1):
    if not is_able[i]:
        count += 1
print(count)