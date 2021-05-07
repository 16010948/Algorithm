CHESS = 8
position = input()
x = ord(position[0]) - ord('a') + 1
y = int(position[1])

moves = ((-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2), (2, 1), (1, 2))

answer = 0
for move in moves:
    nx = x + move[0]
    ny = y + move[1]

    if (nx >= 1 and nx <= CHESS) and (ny >= 1 and ny <= CHESS):
        answer += 1
print(answer)