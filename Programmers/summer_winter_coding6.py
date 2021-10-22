DIRECTION = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}

INDEX = {
    'U': 0,
    'D': 1,
    'R': 2,
    'L': 3
}

DIR_SIZE = 4
SIZE = 5


def is_range(y, x):
    return y >= SIZE * -1 and y <= SIZE and x >= SIZE * -1 and x <= SIZE


def move(dirs):
    route = set()
    x = 0
    y = 0

    for d in dirs:
        nx = x + DIRECTION[d][0]
        ny = y + DIRECTION[d][1]
        if is_range(ny, nx):
            route.add((y, x, ny, nx))
            route.add((ny, nx, y, x))
            x = nx
            y = ny
    return len(route) // 2


def solution(dirs):
    answer = move(dirs)
    return answer