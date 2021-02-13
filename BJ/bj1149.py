n = int(input())

color = []
for i in range(n):
    color.append(list(map(int, input().split())))
    if i > 0:
        color[i][0] += min(color[i - 1][1], color[i - 1][2])
        color[i][1] += min(color[i - 1][0], color[i - 1][2])
        color[i][2] += min(color[i - 1][0], color[i - 1][1])
print(min(color[n - 1]))