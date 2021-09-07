def fill_sudoku(idx):
    if idx == len(blank):
        for y in range(9):
            for x in range(9):
                print(sudoku[y][x], end=" ")
            print()
        exit(0)

    y, x = blank[idx]
    for n in range(1, 10):
        if not (row[y][n] or col[x][n] or squ[y // 3 * 3 + x // 3][n]):
            row[y][n] = True
            col[x][n] = True
            squ[y // 3 * 3 + x // 3][n] = True
            sudoku[y][x] = n
            fill_sudoku(idx + 1)
            row[y][n] = False
            col[x][n] = False
            squ[y // 3 * 3 + x // 3][n] = False
            sudoku[y][x] = 0


sudoku = []
blank = []

row = [[False]*10 for _ in range(9)]
col = [[False]*10 for _ in range(9)]
squ = [[False]*10 for _ in range(9)]

for i in range(9):
    sudoku.append(list(map(int, input().split())))
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append((i, j))
        else:
            row[i][sudoku[i][j]] = True
            col[j][sudoku[i][j]] = True
            squ[i // 3 * 3 + j // 3][sudoku[i][j]] = True

fill_sudoku(0)
