def dfs(n, m, start, result):
    if len(result) >= m:
        print(' '.join(str(r) for r in result))
        return

    for i in range(start, n + 1):
        result.append(i)
        dfs(n, m, i, result)
        result.pop()

n, m = map(int, input().split())
dfs(n, m, 1, [])