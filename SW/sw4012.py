INF = int(1e9)


def cook(value):
    synergy = 0
    for i in range(N):
        if is_selected[i] == value:
            for j in range(N):
                if is_selected[j] == value:
                    synergy += ingredient[i][j]
    return synergy


def power_set(idx, cnt):
    global answer
    if cnt > N / 2:
        return

    if idx == N:
        if cnt == N / 2:
            answer = min(answer, abs(cook(True) - cook(False)))
        return

    is_selected[idx] = True
    power_set(idx + 1, cnt + 1)
    is_selected[idx] = False
    power_set(idx + 1, cnt)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    ingredient = []
    for _ in range(N):
        ingredient.append(list(map(int, input().split())))

    answer = INF
    is_selected = [False] * N
    power_set(0, 0)
    print("#" + str(test_case), answer)