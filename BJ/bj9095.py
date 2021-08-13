NUMBERS = (1, 2, 3)
def dfs(s):
    global count
    if s >= n:
        if s == n:
            count += 1
        return

    for i in range(1, 3 + 1):
        dfs(s + i)

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    dfs(0)
    print(count)