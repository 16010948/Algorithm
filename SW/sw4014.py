HEIGHT = 1


def is_range(r, c):
    return r >= 0 and r < N and c >= 0 and c < N


def vertical_runway_length(r, c, delta, is_able):
    count = 0
    nr = r
    for _ in range(X):
        if not is_range(nr, c) or not is_able[nr][c] or runway[r][c] != runway[nr][c]:
            return False
        is_able[nr][c] = False
        nr += delta
    return True


def check_vertical(runway):
    count = 0
    is_able = [[True] * N for _ in range(N)]

    for i in range(N):
        flag = True
        for j in range(1, N):
            if runway[j - 1][i] == runway[j][i]:
                continue

            if runway[j][i] - runway[j - 1][i] == HEIGHT:
                if not vertical_runway_length(j - 1, i, -1, is_able):
                    flag = False
                    break
            elif runway[j - 1][i] - runway[j][i] == HEIGHT:
                if not vertical_runway_length(j, i, 1, is_able):
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            count += 1
    return count


def horizontal_runway_length(r, c, delta, is_able):
    count = 0
    nc = c
    for _ in range(X):
        if not is_range(r, nc) or not is_able[r][nc] or runway[r][c] != runway[r][nc]:
            return False
        is_able[r][nc] = False
        nc += delta
    return True


def check_horizontal(runway):
    count = 0
    is_able = [[True] * N for _ in range(N)]

    for i in range(N):
        flag = True
        for j in range(1, N):
            if runway[i][j - 1] == runway[i][j]:
                continue

            if runway[i][j] - runway[i][j - 1] == HEIGHT:
                if not horizontal_runway_length(i, j - 1, -1, is_able):
                    flag = False
                    break
            elif runway[i][j - 1] - runway[i][j] == HEIGHT:
                if not horizontal_runway_length(i, j, 1, is_able):
                    flag = False
                    break
            else:
                flag = False
                break
        if flag:
            count += 1
    return count


T = int(input())

for test_case in range(1, T + 1):
    N, X = map(int, input().split())

    runway = []
    for _ in range(N):
        runway.append(list(map(int, input().split())))

    answer = check_vertical(runway) + check_horizontal(runway)
    print("#" + str(test_case), answer)