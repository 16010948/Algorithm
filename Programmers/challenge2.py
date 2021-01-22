DIRECTION = [(0, 1), (1, 0), (-1, -1)]


def solution(n):
    answer = []
    index = 1
    x = 0
    y = -1
    triangle = []

    for i in range(1, n + 1):
        triangle.append([0] * i)

    for i in range(n):
        for j in range(n - i):
            x += DIRECTION[i % 3][0]
            y += DIRECTION[i % 3][1]
            triangle[y][x] = index
            index += 1

    for t in triangle:
        answer += t

    return answer
n = 4
# answer = [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
print(solution(n))

n = 5
# answer = [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
print(solution(n))

n = 6
# answer = [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]
print(solution(n))