import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * (m + 1)]
for y in range(1, n + 1):
    arr.append(list(map(int, input().split())))
    arr[y].insert(0, 0)

s_arr = [[0] * (m + 1)]
for y in range(1, n + 1):
    s_arr.append([0])
    for x in range(1, m + 1):
        s_arr[y].append(s_arr[y][x - 1] + s_arr[y - 1][x] + arr[y][x] - s_arr[y - 1][x - 1])

k = int(input())
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    print(s_arr[y2][x2] - s_arr[y1 - 1][x2] - s_arr[y2][x1 - 1] + s_arr[y1 - 1][x1 - 1])