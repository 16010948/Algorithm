def dfs(n, m, start, result):
    if len(result) == m:
        print(' '.join([str(i) for i in result]))
        return
    for i in range(start, n + 1):
        if i not in result:
            result.append(i)
            dfs(n, m, i + 1, result)
            result.pop()

n, m = map(int, input().split())
dfs(n, m, 1, [])