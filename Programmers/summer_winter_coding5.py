DIRECTION = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}


def solution(dirs):
    answer = 0

    x = 0
    y = 0
    route = set()
    for d in dirs:
        nx = x + DIRECTION[d][0]
        ny = y + DIRECTION[d][1]
        if nx >= -5 and nx <= 5 and ny >= -5 and ny <= 5:
            route.add((x, y, nx, ny))
            route.add((nx, ny, x, y))
            x = nx
            y = ny
    answer = len(route) // 2
    return answer

dirs = "ULURRDLLU"
# answer = 7
print(solution(dirs))

dirs = "LULLLLLLU"
# answer = 7
print(solution(dirs))