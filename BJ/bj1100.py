SIZE = 8
chess = []
for _ in range(SIZE):
    chess.append(input())

answer = 0
for i in range(SIZE):
    for j in range(i % 2, SIZE, 2):
        if chess[i][j] == 'F':
            answer += 1
print(answer)