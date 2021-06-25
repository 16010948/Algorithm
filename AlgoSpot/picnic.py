def dfs(start, remain):
    if not remain:
        return 1

    count = 0
    for i in range(start, n):
        if not visited[i]:
            for j in range(i + 1, n):
                if not visited[j] and relations[i][j]:
                    visited[i] = visited[j] = True
                    count += dfs(i, remain - 2)
                    visited[i] = visited[j] = False
    return count

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    friends = list(map(int, input().split()))

    relations = [[False] * n for _ in range(n)]
    for i in range(m):
        relations[friends[2 * i]][friends[(2 * i) + 1]] = True
        relations[friends[(2 * i) + 1]][friends[2 * i]] = True

    visited = [False] * n
    print(dfs(0, n))