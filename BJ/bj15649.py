def dfs(n, m, result):
    if len(result) == m:
        print(' '.join([str(i) for i in result]))
        return

    for i in range(1, n + 1):
        if i not in result:
            result.append(i)
            dfs(n, m, result)
            result.pop()

n, m = map(int, input().split())
dfs(n, m, [])