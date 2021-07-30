n, m = map(int, input().split())

castle = []
row = [False] * n
col = [False] * m
for i in range(n):
    castle.append(list(input()))
    for j in range(m):
        if castle[i][j]  == 'X':
            row[i] = True
            col[j] = True

row_count = 0
for i in range(n):
    if not row[i]:
        row_count += 1

col_count = 0
for j in range(m):
    if not col[j]:
        col_count += 1

print(max(row_count, col_count))