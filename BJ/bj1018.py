def check_color(matrix):
    count = [0] * 2
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if (i + j) % 2 == 0:
                if col == 'B':
                    count[0] += 1
                else:
                    count[1] += 1
            else:
                if col == 'B':
                    count[1] += 1
                else:
                    count[0] += 1
    return min(count)

answer = 50 * 50 + 1
m, n = map(int, input().split())
matrix = []
for _ in range(m):
    matrix.append(input())

for row in range(m - 7):
    for col in range(n - 7):
        chess = [chess_row[col:col+8] for chess_row in matrix[row:row + 8]]
        answer = min(answer, check_color(chess))
print(answer)