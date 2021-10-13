class Coord:
    def __init__(self, y, x):
        self.y = y
        self.x = x


class BC:
    def __init__(self, y, x, coverage, performance):
        self.location = Coord(y, x)
        self.coverage = coverage
        self.performance = performance


DIRECTION = (
    (0, 0),
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
)
USER = 2
SIZE = 10


def find(usable, bc):
    if usable == 0:
        return -1

    index = -1
    max_performance = 0
    for i in range(len(bc)):
        if (usable & (1 << i)) != 0 and bc[i].performance > max_performance:
            index = i
            max_performance = bc[i].performance
    return index


def max_performance(usable1, usable2, bc):
    index1 = find(usable1, bc)
    index2 = find(usable2, bc)

    performance1 = 0
    if index1 != -1:
        performance1 = bc[index1].performance

    performance2 = 0
    if index2 != -1:
        performance2 = bc[index2].performance

    total = 0
    if index1 != -1 and index2 != -1 and index1 == index2:
        next_performance = 0
        next_index1 = find(usable1 & ~(1 << index1), bc)
        if next_index1 != -1:
            next_performance = max(next_performance, bc[next_index1].performance)

        next_index2 = find(usable2 & ~(1 << index2), bc)
        if next_index2 != -1:
            next_performance = max(next_performance, bc[next_index2].performance)
        total = performance1 + next_performance
    else:
        total = performance1 + performance2
    return total


def charge(state, move, bc, users):
    answer = 0
    for i in range(len(move[0])):
        for j in range(len(users)):
            users[j].y += DIRECTION[move[j][i]][0]
            users[j].x += DIRECTION[move[j][i]][1]
        usable1 = state[users[0].y][users[0].x]
        usable2 = state[users[1].y][users[1].x]
        answer += max_performance(usable1, usable2, bc)
    return answer


def is_range(y, x):
    return y > 0 and y <= SIZE and x > 0 and x <= SIZE


T = int(input())

for test_case in range(1, T + 1):
    M, A = map(int, input().split())
    move = []
    for i in range(USER):
        move.append([0] + list(map(int, input().split())))

    bc = []
    state = [[0] * (SIZE + 1) for _ in range(SIZE + 1)]
    for i in range(A):
        x, y, coverage, performance = map(int, input().split())
        bc.append(BC(y, x, coverage, performance))
        size = 0
        for ny in range(y - coverage, min(y + coverage, SIZE) + 1):
            for nx in range(x - size, min(x + size, SIZE) + 1):
                if is_range(ny, nx):
                    state[ny][nx] = state[ny][nx] | (1 << i)
            if ny < y:
                size += 1
            else:
                size -= 1

    users = []
    users.append(Coord(1, 1))
    users.append(Coord(10, 10))
    answer = charge(state, move, bc, users)
    print("#" + str(test_case), answer)