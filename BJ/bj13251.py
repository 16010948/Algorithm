m = int(input())
color = list(map(int, input().split()))
k = int(input())

total = sum(color)
percentage = [1.0] * m
answer = 0
for i in range(m):
    if color[i] < k:
        percentage[i] = 0
        continue

    percentage[i] = 1.0
    for j in range(k):
        percentage[i] *= (color[i] - j) / (total - j)
    answer += percentage[i]

print(answer)