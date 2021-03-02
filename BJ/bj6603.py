def dfs(array, start, result):
    if len(result) == 6:
        print(' '.join(str(item) for item in result))
        return
    for i in range(start, len(array)):
        if array[i] not in result:
            result.append(array[i])
            dfs(array, i + 1, result)
            result.pop()


while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    dfs(s[1:], 0, [])
    print()