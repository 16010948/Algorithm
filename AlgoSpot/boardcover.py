COVER_TYPE = (
    ((0, 0), (1, 0), (0, 1)),
    ((0, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (1, -1))
)

def set_block(board, x, y, block):
    for dy, dx in block:
        ny = y + dy
        nx = x + dx
        if nx < 0 or nx >= col or ny < 0 or ny >= row:
            return False
        elif board[ny][nx] == "#":
            return False
    return True

def fill_block(board, x, y, block):
    for dy, dx in block:
        ny = y + dy
        nx = x + dx
        board[ny][nx] = '#'

def remove_block(board, x, y, block):
    for dy, dx in block:
        ny = y + dy
        nx = x + dx
        board[ny][nx] = '.'

def cover_block(board):
    x, y = -1, -1
    for i in range(row):
        for j in range(col):
            if board[i][j] == '.':
                y, x = i, j
                break
        if y != -1:
            break
    if y == -1:
        return 1

    ret = 0
    for block in COVER_TYPE:
        if set_block(board, x, y, block):
            fill_block(board, x, y, block)
            ret += cover_block(board)
            remove_block(board, x, y, block)
    return ret

T = int(input())

for test_case in range(1, T + 1):
    row, col = map(int, input().split())

    board = []
    total = 0
    for _ in range(row):
        board.append(list(input().strip()))
        for index in range(col):
            if board[-1][index] == '.':
                total += 1
    if total % 3 != 0:
        result = 0
    else:
        result = cover_block(board)
    print(result)