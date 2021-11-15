def reverse_matrix(y, x):
    for ny in range(3):
        for nx in range(3):
            origin[y + ny][x + nx] = '0' if origin[y + ny][x + nx] == '1' else '1'

n, m = map(int, input().split())

origin = []
for i in range(n):
    origin.append(list(input()))

answer = []
for i in range(n):
    answer.append(list(input()))

count = 0
for i in range(n - 2):
    for j in range(m - 2):
        if origin[i][j] != answer[i][j]:
            count += 1
            reverse_matrix(i, j)

for i in range(n):
    for j in range(m):
        if origin[i][j] != answer[i][j]:
            count = -1
            break
    if count == -1:
        break
print(count)