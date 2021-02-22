def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i > 0 and j > 0 and board[i][j] != 0:
                board[i][j] += min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1])
            answer = max(board[i][j], answer)
    answer *= answer
    return answer

board = [[0, 1, 1, 1], [1, 1, 1, 1],[1, 1, 1, 1], [0, 0, 1, 0]]
# answer = 9
print(solution(board))

board = [[0, 0, 1, 1],[1, 1, 1, 1]]
# answer = 4
print(solution(board))