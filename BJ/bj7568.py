n = int(input())
bulk = []
for _ in range(n):
    bulk.append(tuple(map(int, input().split())))

rank = [1] * n
for i in range(n):
    for j in range(i + 1, n):
        if bulk[i][0] > bulk[j][0]:
            if bulk[i][1] > bulk[j][1]:
                rank[j] += 1
        elif bulk[i][0] < bulk[j][0]:
            if bulk[i][1] < bulk[j][1]:
                rank[i] += 1
for r in rank:
    print(r, end=" ")