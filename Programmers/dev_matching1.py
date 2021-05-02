SQUARE = ((0, 1), (1, 0), (0, -1), (-1, 0))


def rotate_matrix(matrix, query):
    i, j = query[0] - 1, query[1] - 1
    min_element, prev = matrix[i][j], matrix[i][j]
    for diff in SQUARE:
        i += diff[0]
        j += diff[1]
        while i >= query[0] - 1 and j >= query[1] - 1 and i <= query[2] - 1 and j <= query[3] - 1:
            matrix[i][j], prev = prev, matrix[i][j]
            min_element = min(min_element, matrix[i][j])
            i += diff[0]
            j += diff[1]
        i -= diff[0]
        j -= diff[1]
    return min_element


def solution(rows, columns, queries):
    answer = []

    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]
    for query in queries:
        answer.append(rotate_matrix(matrix, query))

    return answer

rows = 6
columns = 6
queries = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
# answer = [8, 10, 25]
print(solution(rows, columns, queries))

rows = 3
columns = 3
queries = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
# answer = [1, 1, 5, 3]
print(solution(rows, columns, queries))

rows = 100
columns = 97
queries = [[1, 1, 100, 97]]
# answer = [1]
print(solution(rows, columns, queries))