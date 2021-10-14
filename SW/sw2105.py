KIND = 100
deltas = ((1, -1), (1, 1), (-1, 1), (-1, -1))

def is_range(y, x):
    return y >= 0 and y < N and x >= 0 and x < N

def dfs(y, x, index, cnt, dessert, start_y, start_x):
    global answer
    ny = y + deltas[index][0]
    nx = x + deltas[index][1]
    if index == len(deltas) - 1 and ny == start_y and nx == start_x:
        answer = max(answer, cnt)
        return

    if is_range(ny, nx) and not dessert[cafe[ny][nx]]:
        dessert[cafe[ny][nx]] = True
        dfs(ny, nx, index, cnt + 1, dessert, start_y, start_x)
        if index < len(deltas) - 1:
            dfs(ny, nx, index + 1, cnt + 1, dessert, start_y, start_x)
        dessert[cafe[ny][nx]] = False

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cafe = []
    for _ in range(N):
        cafe.append(list(map(int, input().split())))

    dessert = [False] * (KIND + 1)
    answer = -1
    for i in range(N - 1):
        for j in range(1, N - 1):
            dessert[cafe[i][j]] = True
            dfs(i, j, 0, 1, dessert, i, j)
            dessert[cafe[i][j]] = False

    print("#" + str(test_case), answer)